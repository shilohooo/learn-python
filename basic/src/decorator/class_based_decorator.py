"""
基于类的装饰器
"""


# 示例：记录方法的调用次数
class CountCallNumber:
    def __init__(self, func):
        self.func = func
        self.call_number = 0

    def __call__(self, *args, **kwargs):
        self.call_number += 1
        print(f'方法调用次数为：{self.call_number}')
        return self.func(*args, **kwargs)


@CountCallNumber
def say_hi(name):
    print(f'Hi! My name is {name}')


say_hi('Tom')
say_hi('Jack')
