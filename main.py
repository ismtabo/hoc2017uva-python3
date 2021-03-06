import emoji
import telepot
from flask import Flask, render_template, request
from flask_ini import FlaskIni
from telepot.delegate import create_open, pave_event_space, per_chat_id
from telepot.loop import MessageLoop

from db import create_comment, get_comments

app = Flask(__name__)
with app.app_context():
    app.iniconfig = FlaskIni()
    app.iniconfig.read('config.ini')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global comments
        comment_title = request.form['title']
        comment_content = request.form['content']
        create_comment(comment_title, comment_content)

    comments = get_comments()
    return render_template('index.html', comments=comments)


class MessageCounter(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        if not 'text' in msg or not msg['text'].startswith('/newcomment'):
            self.sender.sendMessage(emoji.emojize("Sorry, but I can't understand you! :confused:", use_aliases=True))
            return

        text = msg['text'].lstrip()
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

        self.sender.sendMessage(emoji.emojize("Comment added to guestbook. :grin:", use_aliases=True))


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
