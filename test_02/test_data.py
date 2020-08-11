import random
hh={"name":"#name#"}
if hh["name"] == "#name#":
    number = random.randint(1, 10000)
    name = "开发测试平台" + str(number)
    hh=str(hh).replace("#name#", name)
    print(hh)