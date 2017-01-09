import MySQLdb
import MySQLdb.cursors

class DB():
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            db = 'hakoblog',
            cursorclass = MySQLdb.cursors.DictCursor,
        )
        self.conn.autocommit(True)

    def cursor(self):
        return self.conn.cursor()

    def uuid_short(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT UUID_SHORT() as uuid')
            return cursor.fetchone().get('uuid')
