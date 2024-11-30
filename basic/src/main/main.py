"""
python __main__ - 程序入口
如果一个文件被当作独立的脚本来执行，那该脚本的 name 就会被设置为 __main__
如果一个文件被当作模块导入，那 name 就会被设置为文件名称
"""

import greeting

print(f'name of module greeting: {greeting.__name__}')

greeting.greeting()


def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(3, 5))
