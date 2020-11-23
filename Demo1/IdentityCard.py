# 输入身份证号
idCard = input("请输入你的身份证号：\n")
# 获取前17位数字
num1 = idCard[0:16]
# 获取身份证第17位
num2 = idCard[16]
# 判断输入的字符长度
if len(idCard) != 18:
    print("你输入的身份证号码有误")
else:
    # 判断输入的号码符合身份证要求
    if idCard.isdigit() or (num1.isdigit() and idCard.endswith('x') or idCard.endswith('X')):
        num = int(idCard[16])
        # 判断身份证性别
        if num % 2 == 0:
            print("身份证性别为：女")
        else:
            print("身份证性别为：男")
    else:
        print("你输入的身份证号码有误")
