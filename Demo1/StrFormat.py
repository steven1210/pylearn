def strFormat(students_info):
    # 非空判断
    if studentsInfo == 'null':
        print('不能输入空')
    # 切片得到列表
    student_info = students_info.split(';')
    # print(student_info)
    # 循环列表
    for info in student_info:
        # print(info.split(','))
        # 信息为空时不执行
        if ',' not in info:
            continue
        # 切片得到列表
        str_info = info.split(',')
        # print(str_info)
        # 得到名字，并去掉空格
        name = str_info[0].strip()
        # 得到年龄，并去掉空格
        age = str_info[1].strip()
        # 判断年龄为整数
        if age.isdigit():
            # 格式化输入姓名、年龄
            print('{:<20}：{:>02}；'.format(name, age))
        else:
            print("年龄请输入数字。")


# 输入学生信息
studentsInfo = input("请输入学生信息：")
strFormat(studentsInfo)
