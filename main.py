from collections import namedtuple
from flask import Flask, render_template
app = Flask(__name__)

Comment = namedtuple('Comment', ['title', 'content'])

@app.route('/')
def index():
    comments = [
        Comment("First comment", "This page isn't bad at all."),
        Comment("Second comment", "Hi there. Lets start the party!"),
        ...
        ]
    return render_template('index.html', comments=comments)
