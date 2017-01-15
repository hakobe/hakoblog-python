from flask import Flask, render_template
from hakoblog.config import CONFIG


web = Flask(__name__)
web.config.from_object(CONFIG)


@web.route('/')
def index():
    return render_template('index.html')
