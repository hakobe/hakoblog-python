from hakoblog.model.blog import Blog


class BlogLoader():
    @classmethod
    def find_by_id(cls, db, blog_id):
        with db.cursor() as cursor:
            cursor.execute(
                '''
                SELECT id, owner_id, title
                FROM blog
                WHERE id = %s
                LIMIT 1
                ''',
                (blog_id, )
            )
            row = cursor.fetchone()

            if row is None:
                return None

        return Blog(**row)
