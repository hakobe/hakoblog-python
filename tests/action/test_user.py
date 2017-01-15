import tests.hakoblog  # noqa: F401

from nose.tools import eq_

from hakoblog.db import DB
from hakoblog.loader.user import UserLoader
from hakoblog.action.user import UserAction

from tests.util import random_string


def test_create():
    db = DB()

    name = random_string(10)
    UserAction.create(db, name)
    user = UserLoader.find_by_name(db, name)
    eq_(user.name, name)
