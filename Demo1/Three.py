# 计算出1000以内含有3的数字的数量
count = 0
for number in range(10000):
    if '3' in str(number):
        count = count + 1
print(count)
