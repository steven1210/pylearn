# 要求大家用面向对象的设计编写一个python程序，实现一个文字游戏系统。
# 动物园里面有10个房间，房间号从1 到 10。
# 每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
# 游戏开始后，系统随机在10个房间中放入老虎或者羊。
# 然后随机给出房间号，要求游戏者选择敲门还是喂食。
# 如果选择喂食：
# 喂老虎应该输入单词 meat，喂羊应该输入单词 grass
# 喂对了，体重加10斤。 喂错了，体重减少10斤
# 如果选择敲门：
# 敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。
# 游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。
# 游戏3分钟结束后，显示每个房间的动物和它们的体重。
# 分析：
# 1，创建老虎的类
# 2，创建羊的类
# 3，创建房子的类
# 4，把动物放入房间
# 5，其他相关代码
import time  # 导入时间模块
from random import randint  # 导入随机数模块


class Tiger:  # 创建类：Tiger
    def __init__(self):  # 初始化方法
        self.name = '老虎'  # 创建静态属性：name
        self.weight = 200  # 创建静态属性：weight

    def eat(self, food):  # 创建喂食方法
        if food == 'meat':  # 判断喂食的食物种类
            print("老虎的喂食正确，体重加10斤。")
            self.weight += 10
        elif food == 'grass':
            print("老虎的喂食错误，体重减10斤。")
            self.weight -= 10
        else:
            print("食物种类不正确，请输入meat或grass。")

    def called(self):  # 创建动物叫声的方法
        print("老虎的叫声：Wow!!；体重减5斤")
        self.weight -= 5


class Sheep:  # 创建类：Sheep
    def __init__(self):  # 初始化方法
        self.name = '羊'  # 创建静态属性：name
        self.weight = 100  # 创建静态属性：weight

    def eat(self, food):  # 创建喂食方法
        if food == 'meat':  # 判断喂食的食物种类
            print('羊的喂食错误，体重减10斤。')
            self.weight -= 10
        elif food == 'grass':
            print('羊的喂食正确，体重加10斤。')
            self.weight += 10
        else:
            print("食物种类不正确，请输入meat或grass。")

    def called(self):  # 创建动物叫声的方法
        print("羊的叫声：mie~~；体重减5斤。")
        self.weight -= 5


class Room:  # 创建一个房间的类
    def __init__(self, category):  # 动物种类的初始化方法
        self.category = category


roomList = []  # 创建一个list，存放10个房间的实例
for i in range(1, 11):
    if randint(1, 2) == 1:  # 随机1个数字，1代表老虎，2代表羊
        animal = Tiger()  # 实例出一个老虎
    else:
        animal = Sheep()  # 实例出一个羊
    room = Room(animal)  # 将动物放入房间的实例中
    roomList.append(room)  # 将房间的实例放入到列表中

startTime = time.time()  # 记录游戏开始时间
while time.time() - startTime <= 10:  # 判断游戏时间在3分钟内
    roomNum = randint(0, 9)  # 随机一个数
    randint_room = roomList[roomNum]  # 随机一个房间
    knockDoor = input(f'当前访问的{roomNum + 1}号房间，请问是否需要敲门:Y/N;')
    if knockDoor in ('Y', 'y'):  # 敲门
        randint_room.category.called()  # 调用房子实例的动物种类实例的叫声方法
    else:
        print('你没有敲门。')

    feedAnimal = input(f'请问是否需要喂食:Y/N;')
    if feedAnimal in ('Y', 'y'):
        food_animal = input(f'请输入喂食的食物：meat/grass')
        if food_animal == 'meat' or food_animal == 'grass':  # 判断喂食的食物种类
            randint_room.category.eat(food_animal)  # 调用房子实例的动物种类实例的吃的方法
        else:
            print('你喂食的食物种类错误。')
else:
    print('游戏时间到，游戏结束。')  # 游戏时间超过3分钟，结束游戏

for i in range(len(roomList)):  # 遍历10个房间
    print(f'第{i+1}号房间的动物是：{roomList[i].category.name}，'
          f'体重是：{roomList[i].category.weight}')  # 打印出房间的动物的名字和体重
