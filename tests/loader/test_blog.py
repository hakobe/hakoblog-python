from nose.tools import eq_

from hakoblog.db import DB
from hakoblog.loader.blog import BlogLoader

from tests.util import create_user, create_blog

def test_create():
    db = DB()

    user = create_user()
    blog = create_blog(user = user)

    found_blog = BlogLoader.find_by_id(db, blog.id)

    eq_(found_blog.id, blog.id)
