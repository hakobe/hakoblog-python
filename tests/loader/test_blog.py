import tests.hakoblog  # noqa: F401

from hakoblog.db import DB
from hakoblog.loader.blog import BlogLoader

from tests.util import create_user, create_blog


def test_find_by_id():
    db = DB()

    user = create_user()
    blog = create_blog(user=user)

    found_blog = BlogLoader.find_by_id(db, blog.id)

    assert found_blog.id == blog.id

    assert BlogLoader.find_by_id(db, -1) is None


def test_find_by_owner_id():
    db = DB()

    blog = create_blog()

    found_blog = BlogLoader.find_by_owner_id(db, blog.owner_id)

    assert found_blog.id == blog.id

    assert BlogLoader.find_by_owner_id(db, -1) is None
