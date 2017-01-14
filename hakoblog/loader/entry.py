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

    @classmethod
    def find_entries(cls, db, blog_id, limit=30):
        with db.cursor() as cursor:
            cursor.execute(
                '''
                SELECT id, blog_id, title, body, created, modified
                FROM entry
                WHERE blog_id = %s
                ORDER BY created DESC
                LIMIT %s
                ''',
                (blog_id, limit)
            )
            rows = cursor.fetchall()

        return [Entry(**r) for r in rows]
