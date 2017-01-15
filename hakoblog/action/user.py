from datetime import datetime

from hakoblog.config import CONFIG
from hakoblog.loader.user import UserLoader


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

    @classmethod
    def ensure_global_user_created(cls, db):
        global_user_name = CONFIG.HAKOBLOG_USER
        user = UserLoader.find_by_name(db, global_user_name)
        if user is None:
            user = cls.create(db, global_user_name)
        return user
