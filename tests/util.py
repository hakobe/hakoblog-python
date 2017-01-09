import random
import string

from hakoblog.db import DB
from hakoblog.action.user import UserAction
from hakoblog.loader.user import UserLoader

from hakoblog.action.blog import BlogAction
from hakoblog.loader.blog import BlogLoader

def random_string(length, seq=string.digits + string.ascii_letters):
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])


def create_user():
    db = DB()
    name = random_string(10)
    UserAction.create(db, name)
    return UserLoader.find_by_name(db, name)

def create_blog(user = None):
    db = DB()

    if user == None:
        user = create_user()

    new_blog_id = BlogAction.create(db, owner_id = user.id, title = random_string(10))
    return BlogLoader.find_by_id(db, new_blog_id)
