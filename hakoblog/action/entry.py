from datetime import datetime

class EntryAction():
    @classmethod
    def post(cls, db, blog_id, title, body):
        now = datetime.now()
        new_id = db.uuid_short()
        with db.cursor() as cursor:
            cursor.execute(
                '''
                    INSERT INTO entry (
                        id, blog_id, title, body, created, modified
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s
                    )
                ''',
                (new_id, blog_id, title, body, now, now)
            )
        return new_id
