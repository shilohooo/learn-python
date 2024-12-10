"""
python itertools - 一组操作集合/字典迭代器的工具集，高性能，且能有效地利用内存
"""
import itertools
import operator

# accumulate() - 传一个组数据，然后将数据应用到指定的函数中，再根据函数的返回组创建
data = [1, 2, 3, 4, 5, 6, 7]
# 这里使用了 operator.mul，累计乘积
# 1 * 2 * 3 * 4 * 5 * 6 * 7
result = itertools.accumulate(data, operator.mul)
for num in result:
    print(num)

# 累计和：1 + 2 + 3 + 4 + 5 + 6 + 7，如果第二个参数不传，默认就是累计和
# result2 = itertools.accumulate(data, operator.add)
result2 = itertools.accumulate(data)
for num in result2:
    print(num)

print(operator.mul(1, 2))
print(operator.add(1, 2))

# combinations() - 将一组数组拆分成 n 个组合，n = 数组长度，每个组合都是一个元组，元组里面的数组是唯一的，有多少个数组由第二个参数决定
shapes = ['circle', 'triangle', 'square']
shapes_combination_result = itertools.combinations(shapes, 2)
for item in shapes_combination_result:
    # ('circle', 'triangle')
    # ('circle', 'square')
    # ('triangle', 'square')
    print(item)

print("=================================================")

# combinations_with_replacement() - 与 combinations() 的区别是它允许元素重复出现多次
shapes_combination_with_replacement_result = itertools.combinations_with_replacement(shapes, 2)
for item in shapes_combination_with_replacement_result:
    # ('circle', 'circle')
    # ('circle', 'triangle')
    # ('circle', 'square')
    # ('triangle', 'triangle')
    # ('triangle', 'square')
    # ('square', 'square')
    print(item)
