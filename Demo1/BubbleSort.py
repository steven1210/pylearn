# 冒泡排序：
# 1，经典算法，通过算法将数字按照从小到达的排列
# 定义一个list，用于存储成绩数据
grade = [60, 90, 70, 88, 95, 25, 36, 18]

for i in range(len(grade)-1):  # 控制需要循环的次数
    for j in range(len(grade)-i-1):  # 每次循环中
        if grade[j] > grade[j+1]:  # 比较前一个数与后一个数的大小
            grade[j], grade[j+1] = grade[j+1], grade[j]  # 将大数与小数的位置进行互换
print(grade)  # 打印最后的结果
