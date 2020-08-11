import requests
from test_03.comman.logs import Log
from test_03.dobboo_or_http.dubbo_telnet import Dubbo

log = Log("/Users/xiaoff/python/pytest/test_03/logs")
class connect_kinds:
    def __init__(self,url,data,header):
        self.url=url
        self.data=data
        self.header=header

    def http_connect(self,method):
        if method=="POST":
            res=requests.post(url=self.url,json=self.data,headers=self.header)
            return res.json
        elif method=="GET":
            res=requests.get(url=self.url,headers=self.header)
            return res.json()
        elif method=="PUT":
            res=requests.put(url=self.url,json=self.data,headers=self.header)
            return res.json()
        else:
            try:
                res=requests.request(url=self.url,json=self.data,headers=self.header)
                return res.json()
            except Exception as e:
                log.error("无此连接方式，请重试")
                raise e

    def dubbo_connect(self,service_name, method_name, json_data):
        """
            :param:host:本地服务器地址
            :param：port:本地服务器端口号
            :param:service_name:接口路径
            :param:method_name:方法名
            :param:json_data:数据

        """
        #连接到服务器
        conn = Dubbo(self.host, self.port)
        #连接接口
        result = conn.invoke(service_name, method_name, json_data)
        return result







