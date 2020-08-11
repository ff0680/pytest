from ddt import ddt,data
import pytest
from test_03.comman.connect_excel import connect_excel
import requests
from test_03.comman.logs import Log

class Test_register:
    cases=connect_excel("/Users/xiaoff/python/pytest/test_03/data/test_new.xlsx","Sheet1").read_date()
    log=Log("/Users/xiaoff/python/pytest/test_03/logs")
    @pytest.mark.parametrize('case', cases)
    def test_register(self,case):
        case_id=case["case_id"]
        interface=case["interface"]
        method=case["method"]
        url=case["url"]
        data=eval(case["data"])
        self.log.info("正在测试{}模块中的第{}条数据，请求数据：{}".format(interface,case_id,data))
        res1=requests.request(method=method,json=data,url=url)
        res=res1.json()
        self.log.info("响应数据：{}".format(res))


if __name__ == '__main__':
    pytest.main(["-s","-v","test_register.py"])



