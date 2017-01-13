from datetime import datetime
from hakoblog.model.entry import Entry

class EntryLoader():
    @classmethod
    def find_by_id(cls, db, entry_id):
        with db.cursor() as cursor:
            cursor.execute(
                '''
                SELECT id, blog_id, title, body, created, modified
                FROM entry
                WHERE id = %s
                LIMIT 1
                ''',
                (entry_id, )
            )
            row = cursor.fetchone()

            if row is None:
                return None

        return Entry(**row)
