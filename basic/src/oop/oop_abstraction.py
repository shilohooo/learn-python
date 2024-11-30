"""
python 面向对象编程概念 - 抽象
专注于基本功能/特征，无需关注实现细节
抽象让代码更具模块化，提高可读性，和易于维护。

在 python 中，可以用抽象类或接口来实现抽象
抽象类：一个不能直接实例化的类，用于给其他类继承，通常包含抽象方法（只有方法声明，没有具体实现）
抽象方法提供了一个模板，定义了子类应该如何去实现它
抽象可以让开发者为一组相关的类定义一个通用的接口，然后让子类定义它们具体的行为是怎样的

接口：一组方法签名的集合，可以用于定义一组通用的方法，类要兼容接口，就必须实现它定义的方法
多个实现同一接口的类，可以达到互相替换使用的目的

python 没有对抽象类和接口提供内置支持，但可以使用 abc 模块（abstract base class）来实现
该模块提供了 ABC 类和 abstractmethod 装饰器，可以用来定义抽象类和方法
"""

# 示例
# 导入 abc 模块
from abc import ABC, abstractmethod


# 定义一个抽象类，这个类要继承 ABC 类
class Shape(ABC):
    @abstractmethod
    def area(self):
        """
        使用 abstractmethod 装饰器标注的方法，表示该方法是一个抽象方法
        :return:
        """
        pass


# 子类，创建后会提示：Class Rectangle must implement all abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        获取面积
        :return: 矩形的面积
        """
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(type(shape))
    print(shape.area())
