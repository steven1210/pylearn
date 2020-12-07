# 计算三角形的周长和面积
import math


class Trilateral:
    def __init__(self, a, b, c):
        if a + b > c or a + c > b or b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            print("你输入的数不满足三角形要求")

    def area(self):
        return self.a + self.b + self.c

    def perimeter(self):
        p = (self.a + self.b + self.c) * 0.5
        return math.sqrt(p*(p - self.a)*(p - self.b) * (p - self.c))


trilateral = Trilateral(3, 4, 5)
print(trilateral.area())
print(trilateral.perimeter())
