"""
python context manager

通用用于读写文件、帮助应用程序节省内存

比如：with 语句，操作完文件后会自动释放资源
"""

import contextlib

with open('./test.txt', 'w') as writer:
    writer.write('Hello World!!!')


# 自定义一个 context manager
@contextlib.contextmanager
def my_context_manager(num):
    print('进入 context manager')
    yield num + 1
    print('退出 context manager')


# 使用
with my_context_manager(2) as ctx:
    # 执行到 yield 点位时，ctx 对象的值为 context manager 在 yield 后生成的值
    # 比如这里传的是2，yield 后生成的值是3
    print(f'执行到 yield，{ctx=}')


# 基于类的 context manager
class MyContextManager:
    def __enter__(self):
        """
        进入 context manager，可以做点啥
        :return:
        """
        print('进入 context manager')

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出 context manager，可以做点啥
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        print(f'退出 context manager，{exc_type=}，{exc_val=}，{exc_tb=}')


with MyContextManager():
    print('test')
