"""
python - 异常处理
异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，
同时告诉Python发生异常时怎么办。
"""

try:
    # 业务代码
    print(5 / 0)
except ZeroDivisionError:
    # 异常处理
    print('除数不能为零！')
else:
    # 业务代码执行完没有发送异常，会走到这里~ 
    print('没有异常发生。')
finally:
    print('无论是否发生异常，都会执行。')


# 在同一个 except 代码块中处理多个异常
def divide(dividend, divisor):
    try:
        # var = 'str' + 1
        print(dividend / divisor)
    except(ZeroDivisionError, TypeError) as e:
        print(e)


divide(dividend=10, divisor=5)
divide(dividend=10, divisor=0)


#  自定义异常
class MyException(Exception):
    pass


try:
    raise MyException('抛出自定义异常')
except MyException as e:
    print('捕获自定义异常')
