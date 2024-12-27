"""
Python 类型提示 - 元组中的类型标注

@author: shiloh
@date: 2024/12/27 17:37
"""

# tuple 可以接受任意数量的类型参数：
x: tuple[int] = (5,)
y: tuple[int, str] = (5, 'foo')
# 下面的声明会给出一个类型不匹配的警告
# z: tuple[int] = (1, 2, 3)

# 要表示一个可以是 任意 长度的元组，并且其中的所有元素都是相同类型的 T，请使用 tuple[T, ...]。
# 要表示空元组，请使用 tuple[()]。只使用 tuple 作为注解等效于使用 tuple[Any, ...]：
a: tuple[int, ...] = (1, 2, 3, 4)
a = (2, 3)
a = ()

b: tuple[()] = ()
# 下面的声明会给出一个类型不匹配的警告
# b = ('foo')

# c 的类型为：tuple[Any, ...]
c: tuple = ('foo', 'bar')
c = (1, 2, 3)
