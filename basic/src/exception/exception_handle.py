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
