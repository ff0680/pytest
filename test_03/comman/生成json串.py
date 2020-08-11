# 生成json字符串
import json

import fp
import yaml
from test_03.comman.connect_excel import connect_excel


def handle_yaml(file):
    with open(file, "r", encoding="utf-8")as f:
        x = yaml.load(f, Loader=yaml.FullLoader)
        # print(type(x))
        # print("旧数据", x)
        b = str(x).split()  # 字符串按空格分割成列表
        c = "".join(b)  # 使用一个空字符串合成列表内容生成新的字符串
        # print("新数据", c)
        data = json.dumps(eval(c),ensure_ascii=False)
        print(data)


        # 写入最后一行
        connect_excel("/Users/xiaoff/python/pytest/test_03/data/test_new.xlsx", "json").write_excel_lastline(c)


handle_yaml("/Users/xiaoff/python/pytest/test_03/data/生成json串的config.yaml")
