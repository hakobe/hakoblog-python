import tests.hakoblog  # noqa: F401

from flask import url_for
from nose.tools import eq_

from hakoblog.db import DB
from hakoblog.action.blog import BlogAction
from hakoblog.loader.entry import EntryLoader

from tests.util import web_client, global_user, random_string


def test_post_show_form():
    with global_user(random_string(5)):
        res = web_client().get('/-/post')
        eq_(res.status, '200 OK')


def test_post_create_entry():
    db = DB()

    with global_user(random_string(5)), web_client() as wc:
        blog = BlogAction.ensure_global_blog_created(db)

        res = wc.post('/-/post', data=dict(
            title='はろー',
            body='こんにちは',
            blog_id=blog.id,
        ))
        eq_(res.status, '302 FOUND')
        eq_(res.headers['Location'], url_for('index', _external=True))

        entry = EntryLoader.find_entries(db, blog.id, limit=1)[0]

        eq_(entry.title, 'はろー')
        eq_(entry.body, 'こんにちは')


def test_post_create_entry_bad_request():
    with global_user(random_string(5)), web_client() as wc:
        res1 = wc.post('/-/post', data=dict())
        eq_(res1.status, '400 BAD REQUEST')

        res2 = wc.post('/-/post', data=dict(
            title='はろー',
            body='こんにちは',
            blog_id=-1,
        ))
        eq_(res2.status, '400 BAD REQUEST')
