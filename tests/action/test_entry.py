from nose.tools import eq_

from hakoblog.db import DB
from hakoblog.action.entry import EntryAction
from hakoblog.loader.entry import EntryLoader

from tests.util import create_blog

def test_post():
    db = DB()

    blog = create_blog()

    entry_id = EntryAction.post(db,
        blog_id = blog.id,
        title = 'タイトル',
        body = 'こんにちは',
    )

    found_entry = EntryLoader.find_by_id(db, entry_id)
    eq_(found_entry.blog_id, blog.id)
    eq_(found_entry.title, 'タイトル')
    eq_(found_entry.body, 'こんにちは')
