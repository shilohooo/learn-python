"""
python 列表推到式/列表解析式
语法：out_list = [out_expr for out_expr in input_list [if out_expr_condition]]
该语法糖同样使用于 dict、set 等一系列可迭代（iterable）的数据结构
最后的 if 条件判断是可选的
"""

names = ["shiloh", "bruce", "jack", "tom", "rose"]
print(names)
# 基于已存在的列表快速创建新的列表
new_names = [n for n in names]
print(new_names)
# 快速创建包含多个数字的列表
numbers = [i for i in range(1, 10)]
print(numbers)
# 快速创建包含两个数字的元组列表：迭代次数为 n * m
number_tuple_list = [(a, b) for a in range(1, 3) for b in range(1, 3)]
print(number_tuple_list)

# 添加条件：筛选1 - 100内的偶数
even_numbers = [i for i in range(1, 101) if i % 2 == 0]
print(even_numbers)
# if else：名字首字母以 s 开头将首字母转为大写，其他保持原来的值
new_upper_names = [name.title() if name.startswith('s') else name for name in names]
print(new_upper_names)
