import pytest

@pytest.fixture()
def myfixture():

    print("执行前半部分程序")
    yield
    print("执行后半部分程序")

class Test_first:
    def test_one(self,myfixture):
        print("执行test_one")
        assert 1==2

    def test_two(self):
        print("执行test_two")
        assert 1==1

    def test_three(self):
        print("执行test_three")
        assert 1==1

if __name__ == '__main__':
    pytest.main(["--setup-show","-s","test_yield.py"])
    # --setup - show:显示固件的执行顺序