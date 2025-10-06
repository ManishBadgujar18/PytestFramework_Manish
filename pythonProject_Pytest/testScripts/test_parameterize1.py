import pytest


@pytest.mark.parametrize('username', ['Admin', 'admin', '12admin'])
def test_login_Website(username):
    print(username)
    assert username=='Admin'