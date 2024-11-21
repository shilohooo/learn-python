# python 中的类

# 创建和使用类：类名命名规范使用大驼峰命名法
# class-fundamental Cat(object): - python2 创建类的语法
class Cat:
    def __init__(self, name, color):
        """
        初始化

        __init__() 是构造方法，创建类的新实例时 Python 会自动运行它。
        注意构造方法名字必须是这个，是规定好的。

        类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。
        在有些情况下，如设置默认值时，在方法__init__() 内指定这种初始值是可行的;
        如果你对某个属性这样做了，就无需包含为它提供初始值的形参。

        :param name: 猫咪的名称
        :param color: 猫咪的颜色
        """
        # self 用于引用当前实例的属性和方法，它必须作为方法的第一个参数
        self.name = name
        self.color = color
        # 声明实例属性，并赋予默认值
        self.age = 3

    def eat(self):
        """
        模拟猫咪吃食物
        :return:
        """
        print('cat: ' + self.name + ', color: ' + self.color + ', now eat~')

    def run(self):
        print('cat: ' + self.name + ', color: ' + self.color + ', now run~')

    def print_age(self):
        """
        打印猫咪的年龄
        :return:
        """
        print('cat\'s age is ' + str(self.age))

    def set_age(self, age):
        """
        设置猫咪的年龄
        :param age: 年龄
        :return:
        """
        self.age = age


# 类实例化：类名(args?)
my_cat = Cat('Kitty', 'Blue')
# 访问类的实例属性和方法：类实例变量.实现属性/方法()
print(my_cat.name)
print(my_cat.color)
my_cat.eat()
my_cat.run()
my_cat.print_age()

# 修改属性的值
# 第一种方式：直接通过实例变量.属性名称修改，这是最简单的方式
my_cat.age = 4
my_cat.print_age()

# 通过方法修改属性值
my_cat.set_age(2)
my_cat.print_age()
