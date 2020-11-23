# 输入手机号
phone = input("请输入你的手机号：")
# 判断输入字符的长度
if len(phone) == 11:
    # 判断是不是纯数字
    if phone.isdigit():
        # 截断前3位，并转换成整型
        num = int(phone[0:3])
        # 判断是哪个运营商
        if 130 <= num <= 150:
            print("你所输入的手机号的运营商是：移动")
        elif 151 <= num <= 170:
            print("你所输入的手机号的运营商是：联通")
        elif 171 <= num <= 199:
            print("你所输入的手机号的运营商是：电信")
        else:
            print("你所输入的手机号不属于任何运营商")
    else:
        print("输入的手机号错误，请重新输入正确的手机号。")
else:
    print("请输入正确的手机号。")
