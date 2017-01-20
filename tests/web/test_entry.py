import tests.hakoblog  # noqa: F401

from pyquery import PyQuery as pq

from hakoblog.db import DB
from hakoblog.action.blog import BlogAction

from tests.util import web_client, global_user, random_string, create_entry


def test_entry():
    db = DB()
    with global_user(random_string(5)):
        blog = BlogAction.ensure_global_blog_created(db)
        entry = create_entry(blog=blog)

        res1 = web_client().get('/entry/' + str(entry.id))
        assert res1.status == '200 OK'
        d = pq(res1.data)
        print('.entry[data-entry-id="%d"]' % (entry.id, ))
        print(d('.entry[data-entry-id="%d"]' % (entry.id, )))

        res2 = web_client().get('/entry/0')
        assert res2.status == '404 NOT FOUND'
