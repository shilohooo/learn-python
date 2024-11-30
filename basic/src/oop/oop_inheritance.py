"""
python 面向对象编程概念 - 继承
继承可用于代码重用，创建共享的属性和方法，使代码变得更简洁
可以将相同的功能放到父类中去实现，子类继承父类，即可获得该功能
"""


# 示例
# 父类
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal name: {self.name}")

    def speak(self):
        print("")


# 子类，在子类类名后面加上括号，然后在括号里面声明继承的父类
class Dog(Animal):
    # 重写父类的方法
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


dog = Dog("Rover")
dog.speak()

cat = Cat("Whiskers")
cat.speak()
