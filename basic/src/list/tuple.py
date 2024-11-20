"""
python 中的元组
Python将不能修改的值称为不可变的，而不可变的列表被称为元组
元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
"""

foods = ("apple", "orange")
print(foods[0])
print(foods[1])
# 下面这行会报错，元组中的元素是不可变的
# food[1] = "banana"

# 遍历元组，和遍历列表是一样的
for food in foods:
    print(food)
