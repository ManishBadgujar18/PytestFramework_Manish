import pytest

#reason is not mandatory its an option
#@pytest.mark.xfail(reason='unimplemented feature / known issue')
@pytest.mark.smoke
def test_A():
    print("Test case A")
    assert True == False

@pytest.mark.xfail
@pytest.mark.smoke
def test_B():
    print("Test case B")
    assert True == False

@pytest.mark.smoke
#@pytest.mark.xfail
def test_C():
    print("Test case C")
    assert True == True

@pytest.mark.smoke
def test_D():
    print("Test case D")
    assert True == True