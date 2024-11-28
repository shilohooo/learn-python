"""
带参数的装饰器
"""

import functools


def my_decorator_with_parameters(arg):
    """
    自定义的装饰器，可以传参数
    :param arg: 参数
    :return:
    """

    def decorator(func):
        # 存储函数的元数据
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'装饰器的参数是：{arg}')
            print('函数执行之前使用装饰器的参数做点啥~')
            result = func(*args, **kwargs)
            print('函数执行完之后使用装饰器的参数做点啥~')
            return result

        return wrapper

    return decorator


# 使用装饰器
@my_decorator_with_parameters(arg='x')
def foo(bar):
    print(bar)


foo('x')
