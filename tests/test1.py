import pytest


def test_print():
    print("Running test print")

@pytest.mark.negative
def test_fail():
    number=3
    assert number==3

@pytest.mark.skip("Skpi my bug")
def test_skip():
    assert False


@pytest.mark.negative
@pytest.mark.xfail  #xpass this test case will pass
def test_xfail():
    assert True


@pytest.mark.xfail  #xfail this test case will fail
def test_xfail2():
    assert False

@pytest.mark.run(order=1)
@pytest.mark.parametrize("num, output", [(1,8), (2, 16), (3,24), (4, 32)])
def test_multiplication(num, output):
    assert 8*num==output



class TestClassCase:
    def test1(self):
        assert True
    def test2(self):
        assert True
    def test31(self):
        assert True

