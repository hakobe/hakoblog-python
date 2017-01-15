from datetime import datetime

from hakoblog.action.user import UserAction
from hakoblog.loader.blog import BlogLoader


class BlogAction():
    @classmethod
    def create(self, db, owner_id, title):
        now = datetime.now()
        new_id = db.uuid_short()
        with db.cursor() as cursor:
            cursor.execute(
                '''
                    INSERT INTO blog (
                        id, owner_id, title, created, modified
                    ) VALUES (
                        %s, %s, %s, %s, %s
                    )
                ''',
                (new_id, owner_id, title, now, now)
            )
        return new_id

    @classmethod
    def ensure_global_blog_created(cls, db):
        global_user = UserAction.ensure_global_user_created(db)
        blog = BlogLoader.find_by_owner_id(db, global_user.id)

        if blog is None:
            cls.create(db, global_user.id, "%s's blog" % (global_user.name, ))
            blog = BlogLoader.find_by_owner_id(db, global_user.id)

        return blog
