# 求100以内和
summation = 0
for i in range(1, 101):
    summation = summation + i

print(summation)

# 求100以内偶数和
str_sum = 0
for i in range(0, 101, 2):  # 从0开始，每次自增2；这样每次自增后获取的都是偶数
    str_sum = str_sum + i
print(str_sum)

# 求100以内奇数和
str_sum1 = 0
for i in range(1, 101, 2):  # 从1开始，每次自增2；这样每次自增后获取的都是奇数
    str_sum1 = str_sum1 + i
print(str_sum1)
