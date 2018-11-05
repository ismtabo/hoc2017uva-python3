import emoji
import telepot
from flask import Flask, render_template, request
from flask_ini import FlaskIni
from flask_socketio import SocketIO, emit
from telepot.delegate import create_open, pave_event_space, per_chat_id
from telepot.loop import MessageLoop

from db import create_comment, get_comments

app = Flask(__name__)
with app.app_context():
    app.iniconfig = FlaskIni()
    app.iniconfig.read('config.ini')

socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global comments
        comment_title = request.form['title']
        comment_content = request.form['content']
        create_comment(comment_title, comment_content)

    comments = get_comments()
    return render_template('index.html', comments=comments, domain=app.iniconfig.get('flask', 'domain'))


@socketio.on('new_comment')
def new_comment(comment):
    comment_title = comment['title']
    comment_content = comment['content']
    emit('new_comment', {
        'title': comment_title,
        'content': comment_content
    }, broadcast=True)
    create_comment(comment_title, comment_content)


class MessageCounter(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        if 'text' in msg and msg['text'].startswith('/newcomment'):
            self.handle_text_message(msg)
        else:
            self.sender.sendMessage(emoji.emojize("Sorry, but I can't understand you! :confused:", use_aliases=True))

    def handle_text_message(self, msg):
        text = msg['text'].strip()
        
        if ' ' not in text: # Empty message
            self.sender.sendMessage(emoji.emojize("Sorry, but I can't understand you! :confused:", use_aliases=True))
            return

        _, comment = text.split(' ', 1)             # Discard command
        title, *content = comment.split('\n', 1)    # Split comment members

        if not content:
            content = title
            title = msg['from']['first_name']
            if 'last_name' in msg['from']:
                title += " "+msg['from']['last_name']
            title += " says"
        else:
            content = content[0]

        create_comment(title, content)

        emit('new_comment', {
            'title': title,
            'content': content
        }, broadcast=True)

        self.sender.sendMessage(emoji.emojize("Comment added to guestbook. :grin:", use_aliases=True))


try:
    bot = telepot.DelegatorBot(app.iniconfig.get('telegram', 'token'), [
        pave_event_space()(
            per_chat_id(), create_open, MessageCounter, timeout=10
        ),
    ])
    
    # Discard Telegram updates when bot was offline
    updates = bot.getUpdates()
    
    if updates:
        last_update_id = updates[-1]['update_id']
        bot.getUpdates(offset=last_update_id + 1)
    
    # Run telepot bot
    MessageLoop(bot).run_as_thread()
except telepot.exception.TelegramError:
    import sys
    print('Sth wrong happens when trying to run telegram bot', file=sys.stderr)

socketio.run(app, host=app.iniconfig.get('flask', 'host'), port=app.iniconfig.getint('flask', 'port'))
