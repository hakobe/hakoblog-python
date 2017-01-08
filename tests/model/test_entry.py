from datetime import datetime

from hakoblog.model.entry import Entry

def test_init():
    now = datetime.now(),
    entry = Entry(
        id = 0,
        blog_id = 1,
        title = 'こんにちは',
        body = '今日は天気が良いですね。',
        created = now,
        modified = now,
    )
    assert entry.id == 0
    assert entry.blog_id == 1
    assert entry.title == 'こんにちは'
    assert entry.body == '今日は天気が良いですね。'
    assert entry.created == now
    assert entry.modified == now
