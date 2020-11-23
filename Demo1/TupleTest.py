# tuple：元组中的元素不能被修改的
tuple1 = (10, 20, 30, 40, 50, 60, 70)
# 元组中只包含一个元素时，需要在元素后面添加逗号
tuple2 = (11,)
# 打印整个元组
print(tuple1)
# 打印元组中的某个元素
print(tuple1[2])
print(tuple1[1:3])

# 元组是不能修改的，但是可以通过拼接的方式生成新的元组
tuple3 = tuple1 + tuple2
print(tuple3)

# 元组的截取
print(tuple1)
# 回滚元组元素
print(tuple1[::-1])
# 打印下标1，2,3的元素；右边是半闭合的，所以不包含最后这个下标下的元素
print(tuple1[1:4])
# 打印下标2及后面的所有元素
print(tuple1[2:])
# 反向截取时，开始下标是-1；反向截取-2到-5下标扥元素
print(tuple1[-2:-5:-1])
# 反向截取-2之后的元素
print(tuple1[-2::-1])
