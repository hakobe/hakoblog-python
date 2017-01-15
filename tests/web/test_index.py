import tests.hakoblog  # noqa: F401

from nose.tools import eq_
from pyquery import PyQuery as pq

from tests.util import web_client, global_user, random_string


def test_index():
    with global_user(random_string(5)) as global_user_name:
        res = web_client().get('/')
        eq_(res.status, '200 OK')

        d = pq(res.data)
        eq_(d('h1').text(), "%s's blog" % (global_user_name, ))
