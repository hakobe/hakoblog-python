import tests.hakoblog  # noqa: F401

from hakoblog.db import DB
from hakoblog.model.user import User
from hakoblog.loader.user import UserLoader

from tests.util import random_string, create_user


def test_find_by_name():
    db = DB()

    user = create_user()

    found_user = UserLoader.find_by_name(db, user.name)
    assert isinstance(found_user, User)
    assert found_user.name == user.name

    not_found_user = UserLoader.find_by_name(db, random_string(10))
    assert not_found_user is None
