from datetime import datetime

class BlogAction():
    @classmethod
    def create(self, db, owner_id, title):
        now = datetime.now()
        new_id = db.uuid_short()
        with db.cursor() as cursor:
            cursor.execute(
                '''
                    INSERT INTO blog (
                        id, owner_id, title, created
                    ) VALUES (
                        %s, %s, %s, %s
                    )
                ''',
                (new_id, owner_id, title, now.strftime('%Y-%m-%d %H:%M:%S'))
            )
        return new_id