import configparser

class config:
    def __init__(self,conf_path):
        self.conf_path=conf_path

    def read_config(self,section,option):
        conf=configparser.ConfigParser()
        conf.read(self.conf_path)
        return conf.get(section,option)

    def write_config(self,section,option,value):
        """修改并保存在配置文件中"""
        # 创建管理对象
        conf = configparser.ConfigParser()
        conf.read(self.conf_path, encoding='utf-8')
        print(conf.sections())
        # 往section添加key和value
        conf.set(section, option, value)
        items = conf.items(section)
        print(items)  # list里面对象是元祖
        conf.write(open(self.conf_path, "r+", encoding="utf-8"))  # r+模式



