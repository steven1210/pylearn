from random import randint

'''
猜拳游戏：石头剪刀布
1，出拳
    玩家：剪刀、石头、布    电脑：剪刀、石头、布
2，判输赢
    玩家胜、电脑胜、平局
'''
# 玩家：出拳
player = int(input('玩家请出拳：0--剪刀，1--石头，2--布：'))
# 电脑：出拳
computer = randint(0, 2)
# 判断玩家获胜的几种方式
if ((player == 0) and (computer == 2)) or ((player == 1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print(f'玩家出拳：{player},电脑出拳：{computer}；玩家获胜！')
# 判断电脑获胜的几种方式
elif ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print(f'玩家出拳：{player},电脑出拳：{computer}; 电脑获胜！')
# 判断平局
else:
    print(f'玩家出拳：{player},电脑出拳：{computer}; 平局')
