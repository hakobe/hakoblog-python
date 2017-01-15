import tests.hakoblog  # noqa: F401

from nose.tools import eq_

from hakoblog.db import DB
from hakoblog.action.blog import BlogAction
from hakoblog.loader.blog import BlogLoader

from tests.util import random_string, create_user


def test_create():
    db = DB()

    user = create_user()
    title = random_string(10)
    blog_id = BlogAction.create(
        db,
        owner_id=user.id,
        title=title,
    )
    found_blog = BlogLoader.find_by_id(db, blog_id)

    eq_(found_blog.id, blog_id)
    eq_(found_blog.owner_id, user.id)
    eq_(found_blog.title, title)
