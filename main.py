from collections import namedtuple
from flask import Flask, render_template, request
app = Flask(__name__)

Comment = namedtuple('Comment', ['title', 'content'])
comments = [
        Comment("First comment", "This page isn't bad at all."),
        Comment("Second comment", "Hi there. Lets start the party!"),
        ]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global comments
        comment_title = request.form['title']
        comment_content = request.form['content']
        comments.append(Comment(comment_title, comment_content))

    return render_template('index.html', comments=comments)
