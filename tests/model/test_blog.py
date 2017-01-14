from hakoblog.model.blog import Blog


def test_init():
    blog = Blog(
        id=0,
        owner_id=1,
        title='僕のブログ',
    )
    assert blog.id == 0
    assert blog.owner_id == 1
    assert blog.title == '僕のブログ'
