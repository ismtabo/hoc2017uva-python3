from collections import namedtuple
from flask import Flask, render_template, request
from db import create_comment, get_comments

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global comments
        comment_title = request.form['title']
        comment_content = request.form['content']
        create_comment(comment_title, comment_content)

    comments = get_comments()
    return render_template('index.html', comments=comments)
