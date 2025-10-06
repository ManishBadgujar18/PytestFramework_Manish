
import pytest

class TestSmoke:

    @pytest.fixture()
    def setup(self):  #Precondtion
        print('Open the browser >> open my application')

    def testCase1_Login(self,setup):
        print('Test1 -Login Test')
        assert 1==1

    def testCase2_search(self,setup):
        print('Test 2- search')

    def testCase3_listofitems(self,setup):
        print('Test 3- list of items')