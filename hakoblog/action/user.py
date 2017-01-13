from datetime import datetime

class UserAction():
    @classmethod
    def create(self, db, name):
        now = datetime.now()
        new_id = db.uuid_short()
        with db.cursor() as cursor:
            cursor.execute(
                '''
                    INSERT INTO user (
                        id, name, created, modified
                    ) VALUES (
                        %s, %s, %s, %s
                    )
                ''',
                (new_id, name, now, now)
            )
        return new_id
