# 字典迭代
dict = {"蔬菜": "菠菜", "水果": "香蕉", "粮食": "小麦"}
print(iter(dict))  # 得到一个迭代器  <dict_keyiterator object at 0x10ef4ab90>
# 只要一个对象有__iter__方法和__next__方法，那么这个对象就可以叫做迭代器。
# 对一个可迭代对象调用它的__iter__方法，得到的就是迭代器对象。
print(next(iter(dict)))

