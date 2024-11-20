"""
python 中的条件判断：每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试
检查是否相等，用 ==

检查是否不相等，用 !=

数字比较 >、 <、 >=、 <=

多个条件与 and

多个条件或 or

判断列表是否包含某元素 in
"""

num_a = 4
num_b = 1
if num_a > num_b:
    print("great than")

nums = [1, 2, 3, 4, 5, 6]
if 4 in nums:
    print("4 in nums")

if 7 not in nums:
    print("7 not in nums")

# if 语句
# 简单的 if-else
if num_a < num_b:
    print("less than")
else:
    print("great than")

# if-elif-else
if num_a > 5:
    print("great than 5")
elif num_a == 4:
    print("equals 4")
else:
    print("less then 5 or not equals 4")