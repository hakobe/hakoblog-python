from hakoblog.model.user import User
class UserLoader():
    @classmethod
    def find_by_name(cls, db, name):
        with db.cursor() as cursor:
            cursor.execute(
                '''
                SELECT id, name
                FROM user
                WHERE name = %s
                LIMIT 1
                ''',
                (name, )
            )
            row = cursor.fetchone()

            if row is None:
                return None

        return User(**row)
