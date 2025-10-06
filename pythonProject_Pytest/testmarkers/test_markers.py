#PS C:\Users\rp34\PycharmProjects\LearningPython> pytest -v -m "sanity or regression"
#PS C:\Users\rp34\PycharmProjects\LearningPython> pytest -v -m "sanity and regression"
# pytest -v -m regression
# pytest -v -m sanity


import pytest

@pytest.mark.smoke
def test_A():
    print("Test case A")
    assert True == True

@pytest.mark.sanity
def test_B():
    print("Test case B")
    assert True == True

@pytest.mark.sanity
def test_C():
    print("Test case C")
    assert True == True

@pytest.mark.sanity
@pytest.mark.regression
def test_D():
    print("Test case D")
    assert True == True