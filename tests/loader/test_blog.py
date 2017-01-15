import tests.hakoblog  # noqa: F401

from nose.tools import eq_, assert_is_none

from hakoblog.db import DB
from hakoblog.loader.blog import BlogLoader

from tests.util import create_user, create_blog


def test_find_by_id():
    db = DB()

    user = create_user()
    blog = create_blog(user=user)

    found_blog = BlogLoader.find_by_id(db, blog.id)

    eq_(found_blog.id, blog.id)

    assert_is_none(BlogLoader.find_by_id(db, -1))


def test_find_by_owner_id():
    db = DB()

    blog = create_blog()

    found_blog = BlogLoader.find_by_owner_id(db, blog.owner_id)

    eq_(found_blog.id, blog.id)

    assert_is_none(BlogLoader.find_by_owner_id(db, -1))
