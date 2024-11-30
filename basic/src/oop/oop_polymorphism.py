"""
python 面向对象编程概念 - 多态
同一种行为，有不同的表现方式

举例：
1.动物的叫声
狗狗是汪汪汪
猫咪是喵喵喵

2.各种形状的面积计算方式
矩形：长 * 宽
圆：Π * 半径的平方

多态可以分两种：方法重载（method overloading）、方法重写（method overriding）
方法重载是有多个相同名称的方法，但是它们的参数不一样，python 没有直接支持，可通过默认参数和可变长参数实现
方法重写则是子类对在父类定义的方法提供了自己的实现，这允许子类在不修改方法名称或签名的前提下，改变方法的行为
"""


# 示例
# 父类
class Shape:
    # 定义一个抽象方法，让子类决定如何实现它
    def area(self):
        pass


# 子类
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        重写父类的方法
        :return: 矩形的面积
        """
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(type(shape))
    print(shape.area())
