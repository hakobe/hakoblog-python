import MySQLdb
import MySQLdb.cursors
from hakoblog.config import CONFIG

class DB():
    def __init__(self):
        self.conn = MySQLdb.connect(
            db = CONFIG.DATABASE,
            host = CONFIG.DATABASE_HOST,
            user = CONFIG.DATABASE_USER,
            password = CONFIG.DATABASE_PASS,
            cursorclass = MySQLdb.cursors.DictCursor,
        )
        self.conn.autocommit(True)

    def cursor(self):
        return self.conn.cursor()

    def uuid_short(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT UUID_SHORT() as uuid')
            return cursor.fetchone().get('uuid')
