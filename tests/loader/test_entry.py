from nose.tools import eq_, assert_is_instance

from hakoblog.db import DB
from hakoblog.model.entry import Entry
from hakoblog.loader.entry import EntryLoader

from tests.util import create_entry

def test_find_by_id():
    db = DB()
    entry = create_entry()

    found_entry = EntryLoader.find_by_id(db, entry.id)
    assert_is_instance(found_entry, Entry)
    eq_(found_entry.id, entry.id)

    not_found_entry = EntryLoader.find_by_id(db, 10)
    eq_(not_found_entry, None)
