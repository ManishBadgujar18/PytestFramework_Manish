import pytest

def test_A():
    print("Test case A")
    assert True == True

@pytest.mark.skip(reason='not implemented')
def test_B():
    print("Test case B")
    assert True == False

def test_C():
    print("Test case C")
    assert True == False

def test_D():
    print("Test case D")
    assert True == True