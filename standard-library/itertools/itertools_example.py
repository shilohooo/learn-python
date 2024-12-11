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

# count() - 创建一个无限的迭代器，从第一个参数开始，每次迭代加第二个参数
for e in itertools.count(10, 1):
    print(e)
    # 不加终止条件会死循环
    if e > 20:
        break

# cycle() - 循环迭代器，直到遇到终止条件
colors = ["red", "blue", "yellow", "green", "orange"]
# for color in itertools.cycle(colors):
#     # 一直循环，到了末尾后又从头开始
#     print(color)

# chain() - 将多个迭代器组合成一个迭代器，迭代器之间用逗号隔开
print("======================== chain() ======================")
for item in itertools.chain(colors, shapes):
    print(item)

# compress() - 将一个迭代器和一个过滤器结合，只返回过滤器中为 True 的元素
print("======================== compress() ======================")
selections = [True, False, True]
for item in itertools.compress(shapes, selections):
    print(item)

# dropWhile() - 丢弃迭代器中，直到遇到第一个不匹配过滤器的元素，然后返回剩下的元素
print("======================== dropWhile() ======================")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# 删掉小于5的元素，如果当前循环的元素大于5，则停止删除
dp_result = itertools.dropwhile(lambda x: x < 5, numbers)
for num in dp_result:
    print(num)

# filterfalse() - 返回所有不匹配过滤器的元素
print("======================== filterfalse() ======================")
# 过滤掉小于5的数字
fp_result = itertools.filterfalse(lambda x: x < 5, numbers)
for num in fp_result:
    print(num)

# groupby() - 元素分组
print("======================== groupby() ======================")
robots = [
    {"name": "blaster", "faction": "autobot"},
    {"name": "galvatron", "faction": "decepticon"},
    {"name": "jazz", "faction": "autobot"},
    {"name": "metroplex", "faction": "autobot"},
    {"name": "megatron", "faction": "decepticon"},
    {"name": "starcream", "faction": "decepticon"},
]
# key 参数指定按什么分组
for key, group in itertools.groupby(robots, key=lambda x: x['faction']):
    print(key)
    print(list(group))

# islice() - 截取迭代器中的元素，与 slices() 类似
print("======================== islice() ======================")
# 截取前两个元素
islice_result = itertools.islice(colors, 2)
for color in islice_result:
    print(color)

# permutations() - 获取一个迭代器，返回所有可能的排列组合
print("======================== permutations() ======================")
alpha_data = ['a', 'b', 'c']
pm_result = itertools.permutations(alpha_data)
for item in pm_result:
    print(item)

# product() - 笛卡尔积（SQL 关联查）
print("======================== product() ======================")
num_data = [1, 2, 3]
for item in itertools.product(num_data, alpha_data):
    print(item)

# repeat() - 重复生成指定个数的元素
print("======================== repeat() ======================")
for item in itertools.repeat("spam", 4):
    print(item)

# starmap() - 将一个函数应用到一组元组中
print("======================== starmap() ======================")
starmap_data = [(2, 6), (3, 8), (4, 9)]
# 将元组里面的两个元素相乘
for item in itertools.starmap(operator.mul, starmap_data):
    print(item)

# takewhile() - 获取迭代器中的元素，直到遇到不满足指定条件的元素为止
print("======================== takewhile() ======================")
# 取出小于5的数字
for num in itertools.takewhile(lambda x: x < 5, numbers):
    print(num)

# tee() - 根据传入的迭代器创建 N 个迭代器
print("======================== tee() ======================")
colors_a, colors_b = itertools.tee(colors, 2)
for color in colors_a:
    print(color)

for color in colors_b:
    print(color)

# zip_longest() - 创建一个迭代器，将多个迭代器中的元素一一对应，无法对应的使用 fillvalue 填充
print("======================== zip_longest() ======================")
for item in itertools.zip_longest(colors, numbers, fillvalue=None):
    print(item)

# https://www.pythoncheatsheet.org/modules/json-module
