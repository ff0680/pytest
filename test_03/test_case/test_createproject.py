from ddt import ddt,data
import pytest
from test_03.comman.connect_excel import connect_excel
import requests
from test_03.comman.logs import Log
from test_03.comman.read_config import config
import random

class Test_createproject:
    cases=connect_excel("/Users/xiaoff/python/pytest/test_03/data/test_new.xlsx","Sheet1").read_date()
    log=Log("/Users/xiaoff/python/pytest/test_03/logs")
    @pytest.mark.parametrize('case', cases)
    def test_create(self,case):
        case_id=case["case_id"]
        interface=case["interface"]
        method=case["method"]
        url=case["url"]
        if "#name#" in case["data"]:
            number = random.randint(1, 10000)
            name = "开发测试平台" + str(number)
            case["data"] = case["data"].replace("#name#", name)
        data=eval(case["data"])
        self.log.info("正在测试{}模块中的第{}条数据，请求数据：{}".format(interface,case_id,data))
        if interface=="create_project":
            headers=config("/Users/xiaoff/python/pytest/test_03/data/config.ini").read_config("temporary_data","header")
            res1 = requests.request(method=method, json=data, url=url,headers=eval(headers))
        else:
            res1=requests.request(method=method,json=data,url=url)
        res=res1.json()
        self.log.info("响应数据：{}".format(res))
        if interface=="login":
            token=res["token"]
            Authorization1="JWT"+" "+token
            dict={"Authorization":Authorization1 }
            config("/Users/xiaoff/python/pytest/test_03/data/config.ini").write_config("temporary_data","header",str(dict))
        assert res["username"]==data["username"]



if __name__ == '__main__':
    pytest.main(["-s","-v","test_createproject.py"])



