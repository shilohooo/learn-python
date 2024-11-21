"""
python 类 - 继承
一个类继承另一个类时，它将自动获得另一个类的所有属性和方法;原有的类称为父类，而新类称为子类。
子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
"""


# Python2 中的继承
# 父类需要在括号中定义object
# class-fundamental Animal(object):
class Animal:
    """
    动物类
    """

    def __init__(self, name, age):
        """
        初始化
        :param name: 动物的名称
        :param age: 动物的年龄
        """
        print("父类构造函数执行")
        self.name = name
        self.age = age

    def run(self):
        """
        模拟动物奔跑
        :return:
        """
        print(f"Animal {self.name} run~")


class Cat(Animal):
    """
    猫咪类，继承 Animal
    继承语法：class-fundamental ClassName(SuperClassName):
    """

    def __init__(self, name, age):
        """
        初始化
        :param name: 猫咪的名称
        :param age: 猫咪的年龄
        """
        # 调用父类的构造函数，传入所需的初始化数据
        print("子类构造函数执行")
        super().__init__(name, age)
        # Python2 中调用父类的构造方法，需要指定子类名称和self
        # super(Cat, self).__init__(name, age)

    def play(self):
        """
        模拟猫咪在玩耍
        :return:
        """
        print(f"Cat {self.name} play")

    def run(self):
        """
        重写父类的方法，称为重载
        :return:
        """
        print(f"Cat {self.name} run")


# 实例化
my_cat = Cat('Kitty', 2)
my_cat.play()
# 使用子类调用父类的方法，称为多态
my_cat.run()
