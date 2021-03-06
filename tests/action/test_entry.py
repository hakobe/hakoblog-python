import tests.hakoblog  # noqa: F401

from hakoblog.db import DB
from hakoblog.action.entry import EntryAction
from hakoblog.loader.entry import EntryLoader

from tests.util import create_blog, create_entry


def test_post():
    db = DB()

    blog = create_blog()

    entry_id = EntryAction.post(
        db,
        blog_id=blog.id,
        title='タイトル',
        body='こんにちは',
    )

    found_entry = EntryLoader.find_by_id(db, entry_id)
    assert found_entry.blog_id == blog.id
    assert found_entry.title == 'タイトル'
    assert found_entry.body == 'こんにちは'


def test_edit():
    db = DB()

    blog = create_blog()

    entry_id = EntryAction.post(
        db,
        blog_id=blog.id,
        title='タイトルbefore',
        body='こんにちはbefore',
    )

    EntryAction.edit(
        db,
        entry_id=entry_id,
        title='タイトルafter',
        body='こんにちはafter',
    )

    found_entry = EntryLoader.find_by_id(db, entry_id)
    assert found_entry.blog_id == blog.id
    assert found_entry.title == 'タイトルafter'
    assert found_entry.body == 'こんにちはafter'


def test_delete():
    db = DB()

    entry = create_entry()

    EntryAction.delete(db, entry.id)
    found_entry = EntryLoader.find_by_id(db, entry.id)

    assert found_entry is None
