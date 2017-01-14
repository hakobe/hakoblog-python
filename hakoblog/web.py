from flask import Flask, render_template


web = Flask(__name__)


@web.route('/')
def index():
    return render_template('index.html')
