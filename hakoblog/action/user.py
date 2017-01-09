from datetime import datetime

class UserAction():
    @classmethod
    def create(self, db, name):
        now = datetime.now()
        with db.cursor() as cursor:
            cursor.execute(
                '''
                    INSERT INTO user (
                        id, name, created
                    ) VALUES (
                        %s, %s, %s
                    )
                ''',
                (db.uuid_short(), name, now.strftime('%Y-%m-%d %H:%M:%S'))
            )
