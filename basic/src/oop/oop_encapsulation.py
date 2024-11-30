"""
python 中的面向对象编程（OOP） - 封装

隐藏内部实现细节，只对外公开基本信息

在 python 中，可以使用访问修饰符来实现封装
访问修饰符是用来定义类中字段和方法的可访问性的关键字
在 python 中，有三个可用的访问修饰符：public、private、protected
但是，在 python 中，并没有一种显示的方式来定义访问修饰符（比如像Java、C++）
相反，python 使用一种约定，以下划线开头作为前缀来决定访问级别：
_protected_field - 单个下划线作为前缀，表示访问级别为 protected，只有类本身和它的子类可以访问
__private_field - 两个下划线作为前缀，表示访问级别为 private，只能类本身可以访问，就算是子类也不能访问
"""


# 示例
class Person:
    def __init__(self):
        self._name = 'shiloh'
        self.__age = 26


person = Person()
# 允许访问，但违反了约定，受保护的字段应该仅在类本身和它的子类中使用
print(person._name)
# 不能访问，报错：AttributeError，私有字段只有类本身可以访问
print(person.__age)
