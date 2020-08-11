# # import copy
# #
# # srcList = ["aaa", "bbb", "ccc", ["a", "b", "c"]]
# # print("原始数据", srcList)
# #
# # # 直接赋值
# # a1 = srcList
# # # 浅赋值
# # a2 = copy.copy(srcList)
# # # 深copy
# # a3 = copy.deepcopy(srcList)
# #
# # srcList[0] = srcList0
# # srcList[3].append(4)
# #
# # #srcList[3]=[1,2,3,4]
# # print("原始数据修改后", srcList)
# # print("直接赋值=", a1)
# # print("浅copy=", a2)
# # print("深copy=", a3)
# import sys
#
# # aList = [1, 2, 3, 4, 5, 6]
# #
# # # for---in
# # #for i in aList:
# # #    print(i, end="")
# #
# # print()
#
# #for j in range(len(aList)):
# #    print(j, end="")
#
# # iterator = iter(aList)
# # #print(iterator.__next__())
# # # print(iterator.__next__())
# # # print(iterator.__next__())
# # # print(iterator.__next__())
# #
# #
# # while True:
# #     try:
# #         print(next(iterator))
# #         aList.pop(2)
# #     except StopIteration:
# #         sys.exit()
#
# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

try:
    assert 1==2
except Exception as e:
    raise e
else:

finally:
    print('finally')
def aa():
    print('else 可以return')
def bb():
    print('finally 可以return')
