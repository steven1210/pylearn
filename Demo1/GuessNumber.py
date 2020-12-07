# 菜数字。随机生成1个1-100之间的数字，用户猜，如果猜对了，游戏结束。
# 如果猜错了给出对应的提示，您输入的值过大，你输入的值过小，最多允许猜7次。
from random import randint

count = 0
number = randint(0, 100)

for count in range(7):
    inNum = input("请输入你猜的数字：")
    if not inNum.isdigit():
        print("请输入数字")
        continue
    if count == 7:
        print("游戏最多猜7次，游戏结束")
        break
    if int(inNum) == number:
        print("恭喜你猜对了，游戏结束")
        break
    elif int(inNum) > number:
        print("您输入的值过大")
        count = count + 1
    else:
        print("您输入的值过小")
        count = count + 1
