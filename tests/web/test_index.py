import tests.hakoblog  # noqa: F401

from nose.tools import eq_, assert_regex
from pyquery import PyQuery as pq

from tests.util import web_client


def test_index():
    res = web_client().get('/')
    eq_(res.status, '200 OK')

    d = pq(res.data)
    assert_regex(d('h1').text(), r'Welcome')
