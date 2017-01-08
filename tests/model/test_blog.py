from datetime import datetime

from internblog.model.blog import Blog

def test_init():
    now = datetime.now(),
    blog = Blog(
        id = 0,
        owner_id = 1,
        title = '僕のブログ',
        created = now,
        modified = now,
    )
    assert blog.id == 0
    assert blog.owner_id == 1
    assert blog.title == '僕のブログ'
    assert blog.created == now
    assert blog.modified == now
