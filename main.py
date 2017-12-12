from collections import namedtuple
from flask import Flask, render_template
app = Flask(__name__)

Comment = namedtuple('Comment', ['title', 'content'])

@app.route('/')
def hello_world():
    comment = Comment("First comment", "This page isn't bad at all.")
    return render_template('index.html', comment=comment)
