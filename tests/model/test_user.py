from hakoblog.model.user import User
def test_init():
    user = User(
        id = 0,
        name = 'hakobe932'
    )
    assert user.id == 0
    assert user.name == 'hakobe932'
