"""
python 中的函数：Python 用关键字 def 来定义函数，函数名以冒号 : 结尾，冒号之后的缩进里的内容都是函数体。
"""


def greeting(msg="World"):
    print("Hello, " + msg.title())


# 函数调用
greeting()
greeting("shiloh")

"""
函数参数：向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同;
也可使用关键字实参，其 中每个实参都由变量名和值组成;还可使用列表和字典。
位置实参：调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
"""


def print_student(name, age):
    print("Hello, my name is " + name.title() + ", I am " + str(age) + " years old")


# 按照形参定义的顺序传递的实参就称为位置实参
print_student("shiloh", 26)

"""
关键字实参：
关键字实参是传递给函数的名称—值对。
关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
用关键字实参指明传递的是哪一个，即使顺序写乱了得到的结果也不会乱。
"""
print_student(age=23, name='tom')

"""
参数默认值
编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值;
否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。
使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
"""


# 注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
# 这让Python依然能够正确地解读位置实参。
def print_student2(name, age=18):
    print('Hello, My name is ' + name.title() + ', I am ' + str(age) + ' years old.')


# 此处调用没有指定 age 参数的值，因此它会使用默认值 18
print_student2('jack')
# 覆盖默认值
print_student2('bruce', 26)

"""
函数返回值：
函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。
函数返回的值被称为返回值。在函数中，可使用return语句将值返回到调用函数的代码行。
返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
"""


def get_student_name(name):
    return name.title()


student_name = get_student_name('thomas')
print(student_name)


# 返回字典类型的数据
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构
def build_person(name, age):
    person = {'name': name, 'age': age}
    return person


person_info = build_person('shiloh', 26)
print(person_info)


# 传递任意数量的实参：Python允许函数从调用语句中收集任意数量的实参
# 形参名 *args 中的星号让 Python 创建一个名为 args 的空元组
# 并将收到的所有值都封装到这个元组中
def print_args(*args):
    """
    打印任意数量的实参
    :param args: 形参列表
    """
    print(args)


print_args('a', 'b', 'c')


def print_args_with_kwargs(name, *args):
    """
    位置实参 + 任意数量实参：

    如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。

    Python 先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

    :param name: 姓名
    :param args: 任意数量的实参
    """
    print('name: ' + name)
    print('other args:')
    for arg in args:
        print(arg)


print_args_with_kwargs('shiloh', 'age', 'email')


def build_person_with_args(first_name, last_name, **args):
    """
    使用任意数量的关键字实参来构建人员信息：

    有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。

    在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。

    一个这样的示例是创建用户简介:你知道你将收到有关用户的信息，但不确定会是什么样的信息。

    :param first_name: 名字
    :param last_name: 姓氏
    :param args: 其他人员信息
    :return:
    """

    person = {'first_name': first_name, 'last_name': last_name}
    for key, val in args.items():
        person[key] = val

    return person


p = build_person_with_args('bruce', 'lee', gender='male', age=30)
print(p)
