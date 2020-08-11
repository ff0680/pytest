import pytest

@pytest.fixture()
def myfixture(request):
    print("执行myfixture方法: %s" %request.param)
    return "你好"

class Test_pytest:
    params1=["1","2","3"]
    @pytest.mark.xfail
    @pytest.mark.parametrize("myfixture", params1,indirect=True)
    def test_one(self, myfixture):
        print("执行test_one %s", myfixture)
        assert 1 == 1

    def test_two(self):
        print("执行test_two")
        assert 1 == 1

    def test_three(self):
        print("执行test_three")
        assert 1 == 1

if __name__ == '__main__':
    pytest.main(["-s" ,"fixture参数化.py"])

