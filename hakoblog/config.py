import os


class Config:
    """Extendable configuation class.
    This is also used for flask application config.
    """

    DATABASE = "hakoblog"
    DATABASE_HOST = "db"
    DATABASE_USER = "root"
    DATABASE_PASS = ""
    TESTING = False
    GLOBAL_USER_NAME = "hakobe"


class Test(Config):
    DATABASE = "hakoblog_test"
    TESTING = True


def config():
    if os.getenv("HAKOBLOG_ENV") == "test":
        return Test()
    else:
        return Config()


CONFIG = config()
