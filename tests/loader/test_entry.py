from nose.tools import eq_, assert_is_instance
from freezegun import freeze_time

from hakoblog.db import DB
from hakoblog.model.entry import Entry
from hakoblog.loader.entry import EntryLoader

from tests.util import create_entry, create_blog


def test_find_by_id():
    "EntryLoader.find_by_id() can find a entry by id"
    db = DB()
    entry = create_entry()

    found_entry = EntryLoader.find_by_id(db, entry.id)
    assert_is_instance(found_entry, Entry)
    eq_(found_entry.id, entry.id)

    not_found_entry = EntryLoader.find_by_id(db, 10)
    eq_(not_found_entry, None)


def test_find_entries():
    "EntryLoader.find_entries can find entries for the specified blog"
    db = DB()
    blog = create_blog()

    entries = []
    with freeze_time('2017-01-13 12:00:02'):
        entries.append(create_entry(blog=blog))
    with freeze_time('2017-01-13 12:00:01'):
        entries.append(create_entry(blog=blog))
    with freeze_time('2017-01-13 12:00:00'):
        entries.append(create_entry(blog=blog))

    found_entries = EntryLoader.find_entries(db, blog.id)
    eq_(len(found_entries), len(entries))
    eq_([e.id for e in found_entries], [e.id for e in entries])

    found_entries_with_limit = EntryLoader.find_entries(db, blog.id, limit=2)
    eq_(len(found_entries_with_limit), len(entries[0:2]))
    eq_([e.id for e in found_entries_with_limit], [e.id for e in entries[0:2]])
