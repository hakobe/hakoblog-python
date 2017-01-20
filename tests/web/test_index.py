import tests.hakoblog  # noqa: F401

from pyquery import PyQuery as pq
from freezegun import freeze_time

from hakoblog.db import DB
from hakoblog.action.blog import BlogAction

from tests.util import web_client, global_user, random_string, create_entry


def test_index():
    with global_user(random_string(5)) as global_user_name:
        res = web_client().get('/')
        assert res.status == '200 OK'

        d = pq(res.data)
        assert d('h1').text() == "%s's blog" % (global_user_name, )


def test_index_with_entries():
    db = DB()
    with global_user(random_string(5)):
        blog = BlogAction.ensure_global_blog_created(db)

        entries = []
        with freeze_time('2017-01-13 12:00:02'):
            entries.append(create_entry(blog=blog))
        with freeze_time('2017-01-13 12:00:01'):
            entries.append(create_entry(blog=blog))
        with freeze_time('2017-01-13 12:00:00'):
            entries.append(create_entry(blog=blog))

        res = web_client().get('/')
        assert res.status == '200 OK'

        d = pq(res.data)

        assert [
            int(d(a).attr('data-entry-id')) for a in d('.entry')
        ] == [e.id for e in entries]
