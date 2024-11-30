"""
python decorator - 装饰器：扩展函数或类的功能

可以理解为 Java 中的代理
"""

import functools


# 一个简单的装饰器示例：接收一个函数作为参数，返回一个包装后的函数
def my_simple_decorator(func):
    def wrapper(*args, **kwargs):
        """
        带参数的包装后的函数
        :param args 可变长参数列表
        :param kwargs 单个或任意多个属性的字典参数
        :return:
        """

        # 在函数执行前做点什么
        print('函数执行前。。。')
        func(*args, **kwargs)
        # 在函数执行完之后做点什么
        print('函数执行完之后。。。')

    return wrapper


# 使用装饰器
@my_simple_decorator
def foo(name):
    """
    被装饰器包装的函数
    :param name: 用户姓名
    :return:
    """

    print(f'My name is {name}')


foo('shiloh')


# 一个通用的装饰器：可带参数，带返回值，也可以都没有
def common_log_decorator(func):
    # functools.wraps 这个装饰器是用来保存函数的元数据的
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        包装函数，可以用来记录日志，比如记录函数的执行时间、参数、返回值等
        :param args: 参数列表
        :param kwargs: 字典，可以传1个或多个自定义的属性
        :return:
        """

        print('函数执行前。。。')
        result = func(*args, **kwargs)
        print('函数执行完之后。。。')
        return result

    return wrapper


@common_log_decorator
def greeting(msg):
    print(f"Hello, {msg}")


greeting('world'.title())
