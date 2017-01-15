from flask import Flask, render_template, g as flask_g

from hakoblog.db import DB
from hakoblog.config import CONFIG
from hakoblog.action.blog import BlogAction


web = Flask(__name__)
web.config.from_object(CONFIG)


def get_db():
    db = getattr(flask_g, '_database', None)
    if db is None:
        db = flask_g._database = DB()
    return db


@web.teardown_appcontext
def close_connection(exception):
    db = getattr(flask_g, '_database', None)
    if db is not None:
        db.close()


@web.route('/')
def index():
    blog = BlogAction.ensure_global_blog_created(get_db())

    return render_template('index.html', blog=blog)
