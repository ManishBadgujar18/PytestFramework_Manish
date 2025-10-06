import pytest


@pytest.fixture()
def setup():
    print('open the browser')
    yield
    print('close the browser')