from flask import (
    Flask,
    g as flask_g,
    render_template,
    request, abort, url_for, redirect,
)

from hakoblog.db import DB
from hakoblog.config import CONFIG
from hakoblog.action.blog import BlogAction
from hakoblog.loader.entry import EntryLoader
from hakoblog.action.entry import EntryAction


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

@web.after_request
def add_secure_headers(response):
    print(response)
    response.headers.add('X-Frame-Options', 'DENY')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1;mode=block')
    response.headers.add('Content-Security-Policy', "default-src 'self'")
    return response


@web.route('/')
def index():
    blog = BlogAction.ensure_global_blog_created(get_db())
    entries = EntryLoader.find_entries(get_db(), blog.id, limit=5)

    return render_template('index.html', blog=blog, entries=entries)


@web.route('/entry/<int:entry_id>')
def entry(entry_id):
    blog = BlogAction.ensure_global_blog_created(get_db())

    entry = EntryLoader.find_by_id(get_db(), entry_id)
    if entry is None:
        abort(404)
    if entry.blog_id != blog.id:
        abort(403)

    return render_template('entry.html', blog=blog, entry=entry)


@web.route('/-/post', methods=['GET'])
def post_get():
    blog = BlogAction.ensure_global_blog_created(get_db())

    return render_template('post.html', blog=blog)


@web.route('/-/post', methods=['POST'])
def post_post():
    blog = BlogAction.ensure_global_blog_created(get_db())

    title = request.form['title']
    body = request.form['body']
    blog_id = int(request.form['blog_id'])

    if int(blog_id) != blog.id:
        abort(400)

    EntryAction.post(
        get_db(),
        blog_id=blog.id,
        title=title,
        body=body,
    )

    return redirect(url_for('index'))
