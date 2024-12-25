"""
Python 类型提示 Demo

@author: shiloh
@date: 2024/12/25 16:00
"""
from typing import TypeAlias, NewType


# region 函数参数与返回值

def get_sum(a: int, b: int) -> int:
    """
    求两个数的和
    :param int a: 第一个数字
    :param int b: 第二个数字
    :return: 两个数的和
    """
    return a + b


# endregion

# region 类型别名

# 类型别名定义：type 类型别名 = 类型
type MyInteger = int
# 类型别名可以用来简化代码
type Movies = list[dict[str, str]]
type Address = tuple[str, int]
# 注意：只有在 3.12 以及后面的版本才能使用 type 语句来声明类型别名，如果版本低于 3.12，则直接赋值即可
# MyMovies = list[dict[str, str]]
# 或者使用 TypeAlias 标记
MyMovies: TypeAlias = list[dict[str, str]]
_a: MyMovies = []

# endregion

# region NewType

UserId = NewType('UserId', int)
user_id = UserId(123)
# user_id2: UserId = 123
# UserId 与 int 是不同的类型，可以看作是原始类型的子类，它可以转换为 int 类型
user_id2: int = user_id

# 可以在 NewType 的基础上继续 NewType
ProUserId = NewType('ProUserId', UserId)


# endregion

# region 标注可调用对象

# 函数 - callable([str, None]) - 表示一个接受 str 类型的单个形参且没有返回值的函数
# 有多个参数 - callable([[int, str], None])
# 有多个参数，且有返回值 - callable([[int, str], str])
# 任意多个形参 - callable([..., None])
def call(greeting: callable([str, None])) -> None:
    """
    调用指定函数
    :param greeting: 要调用的函数
    """
    greeting()


# endregion

# region 变量与返回值

def main():
    """
    程序入口函数，如果没有给返回值添加类型，默认为：None
    """

    # 给变量添加类型
    num_a: int = 1
    num_b: MyInteger = 2
    # 返回值的类型可以自动推导出来
    result = get_sum(num_a, num_b)
    print(f'{result=}')

    print(f'{user_id is int=}')
    print(f'{isinstance(user_id, int)=}')

    # 通过 lambda 声明一个匿名函数
    call(lambda: print('hello world'))


# endregion


if __name__ == '__main__':
    main()
