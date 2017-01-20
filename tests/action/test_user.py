import tests.hakoblog  # noqa: F401

from hakoblog.db import DB
from hakoblog.loader.user import UserLoader
from hakoblog.action.user import UserAction

from tests.util import random_string, global_user


def test_create():
    db = DB()

    name = random_string(10)
    UserAction.create(db, name)
    user = UserLoader.find_by_name(db, name)
    assert user.name == name


def test_ensure_global_user_created():
    db = DB()

    with global_user(random_string(10)) as global_user_name:
        assert UserLoader.find_by_name(db, global_user_name) is None

        user = UserAction.ensure_global_user_created(db)
        assert user.name == global_user_name

        # Check no exceptions raises
        user_again = UserAction.ensure_global_user_created(db)
        assert user_again.id == user.id
