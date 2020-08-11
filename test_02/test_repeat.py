import pytest


@pytest.mark.repeat(2)
class Test_first():


    def test_one(self):
        print("执行test_one")
        assert 1==1

    def test_two(self):
        # test_three(self)
        print("执行test_two")
        assert 1==2


if __name__ == '__main__':
    pytest.main(["-s","-v","-n","4","--looponfail","test_repeat.py"])  #0.63
    # pytest.main(["-s","-v","test_repeat.py"])


    # allure generate test_01/test_01 -0 test_01