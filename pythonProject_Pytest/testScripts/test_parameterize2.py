import pytest

@pytest.mark.parametrize('input, output', [(2,4),(3,9),(4,17)])
def test_square(input,output):
    assert (input**2)==output
