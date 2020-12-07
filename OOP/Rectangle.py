class Rectangle:  # 定义一个长方形的类
    def __init__(self, length, width):  # 初始化方法
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width)*2


rectangle = Rectangle(3, 5)
print(rectangle.area())
print(rectangle.perimeter())
