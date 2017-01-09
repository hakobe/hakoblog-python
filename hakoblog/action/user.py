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
                        id, name, created
                    ) VALUES (
                        %s, %s, %s
                    )
                ''',
                (new_id, name, now.strftime('%Y-%m-%d %H:%M:%S'))
            )
        return new_id
