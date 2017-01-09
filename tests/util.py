import random
import string

from hakoblog.db import DB
from hakoblog.action.user import UserAction
from hakoblog.loader.user import UserLoader

def random_string(length, seq=string.digits + string.ascii_letters):
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])


def create_user():
    db = DB()
    name = random_string(10)
    UserAction.create(db, name)
    return UserLoader.find_by_name(db, name)
