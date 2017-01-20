import tests.hakoblog  # noqa: F401

from hakoblog.db import DB
from hakoblog.loader.user import UserLoader
from hakoblog.action.blog import BlogAction
from hakoblog.loader.blog import BlogLoader

from tests.util import random_string, create_user, global_user


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

    assert found_blog.id == blog_id
    assert found_blog.owner_id == user.id
    assert found_blog.title == title


def test_ensure_global_blog_created():
    db = DB()

    with global_user(random_string(10)) as global_user_name:
        assert UserLoader.find_by_name(db, global_user_name) is None

        blog = BlogAction.ensure_global_blog_created(db)

        found_user = UserLoader.find_by_name(db, global_user_name)
        assert blog.owner_id == found_user.id

        # Check no exeception raises
        blog_again = BlogAction.ensure_global_blog_created(db)
        assert blog_again.id == blog.id
