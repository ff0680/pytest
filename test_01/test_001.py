import pytest
# from test_01.test_自定义标签 import web,android
import allure

import os

# @allure.step("被调用的函数")
# def test_three(self):
#     print("执行test_three")
#     assert 1 == 1


@allure.feature("产品需求")
class Test_first():

    @allure.story('用户场景')
    def test_one(self):
        print("执行test_one")
        assert 1==1


    def test_two(self):
        # test_three(self)
        print("执行test_two")
        assert 1==1


if __name__ == '__main__':
    pytest.main(["-s","-q","--lf","--alluredir","test_01","test_001.py"])

    # allure generate test_01/test_01 -0 test_01