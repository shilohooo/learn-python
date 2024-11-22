"""
python 数据结构 - Set
Set 是包含一系列不重复数据的集合，且是无序的
"""

# 有两种方式可以初始化 set 集合
# 1.使用大括号 {}，如果要创建一个空的 set，需要使用第二种方式

# 使用 {} 创建空的 set 将会得到一个空的字典
empty_set = {}
# 下面这行代码会输出 <class 'dict'>
print(type(empty_set))

# set 会自动移除重复的元素
set1 = {1, 2, 3, 4, 4, 1}
print(set1)

# set 是无序的，因此不能通过索引访问，下面这行代码会报错
# print(set1[0])

# 2.使用内置的 set() 函数
set2 = set()
print(set2)

# 添加或更新 set 里面的元素
set1.add(5)
print(set1)
# 更新多个元素
set1.update([2, 3, 4, 5, 6, 7, 8])
print(set1)

# 移除 set 里面的元素
# 1. 使用 remove() 函数
set1.remove(2)
# 需要注意的是：remove() 在移除一个不存在的元素时会报错
# set1.remove(10)
print(set1)
# 2. 使用 discard() 函数
set1.discard(3)
set1.discard(9)
print(set1)

# set union（并集）
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
s3 = s1.union(s2)
print("======================== union result =====================")
print(s3)
# 还可以使用 | 符号来取并集
print(s1 | s2)

# set intersection（交集）
s4 = {1, 2, 3, 4}
s5 = {3, 4, 5, 6}
s6 = s4.intersection(s5)
print("======================== intersection result =====================")
print(s6)
# 还可以使用 & 符号来取交集
print(s4 & s5)

# set difference（差集）
s7 = {1, 2, 3, 4}
s8 = {1, 3, 5, 6}
s9 = s7.difference(s8)
print("======================== difference result =====================")
print(s9)
# 还可以使用 - 符号来取差集
print(s7 - s8)
