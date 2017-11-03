import tests.hakoblog  # noqa: F401

from tests.util import web_client, global_user, random_string


def test_security_header():
    with global_user(random_string(5)):
        res = web_client().get('/')
        assert res.status == '200 OK'
        assert res.headers['X-Frame-Options'] == 'DENY'
        assert res.headers['X-Content-Type-Options'] == 'nosniff'
        assert res.headers['X-XSS-Protection'] == '1;mode=block'
        assert res.headers['Content-Security-Policy'] == "default-src 'self'"
