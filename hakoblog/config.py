import os

class Config():
    DATABASE = 'hakoblog'
    DATABASE_HOST = 'localhost'
    DATABASE_USER = 'root'
    DATABASE_PASS = ''

class Test(Config):
    DATABASE = 'hakoblog_test'


def config():
    if os.getenv('HAKOBLOG_ENV') == 'test':
        return Test()
    else:
        return Config()

CONFIG = config()
