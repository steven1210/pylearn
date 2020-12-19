import math
from functools import reduce

# 方法1：调用factorial函数
# print(math.factorial(0))


# 方法2：递归调用
# def number(i):
#     if i < 0:
#         print('负数没有阶乘')
#     elif i == 0:
#         return 1
#     else:
#         return i * number(i - 1)
#
#
# print(number(3))


# 方式3：使用for循环
# def number(n, num):
#     if n < 0:
#         print('负数没有阶乘！')
#     elif n == 0:
#         return 1
#     else:
#         for i in range(1, n + 1):
#             num *= i
#         return num
#
#
# print(number(4, 1))


# 从functools中调用reduce()函数
# 使用lambda，匿名函数，迭代
def number(m, n):
    num = reduce(lambda x, y: x*y, range(m, n))
    return num


print(number(1, 4))
