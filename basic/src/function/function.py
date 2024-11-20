"""
python 中的函数：Python 用关键字 def 来定义函数，函数名以冒号 : 结尾，冒号之后的缩进里的内容都是函数体。
"""


def greeting(msg="World"):
    print("Hello, " + msg.title())


# 函数调用
greeting()
greeting("shiloh")

# 函数参数：向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同;
# 也可使用关键字实参，其 中每个实参都由变量名和值组成;还可使用列表和字典。
# 位置实参：调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
# 为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。


def print_student(name, age):
    print("Hello, my name is " + name.title() + ", I am " + str(age) + " years old")


print_student("shiloh", 26)
