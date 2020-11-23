from typing import List

list1 = [10, 20, 30, 40, 50]
# 打印列表
print(list1)
print(list1[1])
print(list1[2:4])
print(list1[3:])
print(list1[::-1])

# 修改列表的值
list1[2] = 60
print(list1)
list1[2:4] = [70, 90]
print(list1)

# 对列表添加值
list2 = [10, 22, 33, 44]
# 此处不建议使用append方法，性能太低;使用append方法插入的值都会在列表的最后
# list2.append(67)
# print(list2)

# 使用insert方法插入数据可以插入到列表的指定位置
list2.insert(3, 99)
print(list2)
# 如果插入的下标超过数组的下标，就插入到最后
list2.insert(7, 100)
print(list2)

# 列表拼接
list3 = [11, 22, 33, 55]
list4 = [66, 77]
list3.extend(list4)
print(list3)
list3.extend('b')
print(list3)

# 列表删除
list5 = [21, 31, 41, 51, 61, 71]
print(list5)
# 使用pop()方法删除列表中指定下标的元素
list5.pop(3)
print(list5)
# 使用remove方法删除列表中指定的元素
list5.remove(31)
print(list5)
# 使用del方法删除列表中指定下标的元素
del list5[2]
print(list5)
# 如果不带下标，就删除整个列表
# del list5
# print(list5)
