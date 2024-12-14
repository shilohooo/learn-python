"""
python 标准库 - random

该模块主要用于生成随机元素
"""

import random

# 初始化
# random.seed(1)
# 生成 0. - 1.0 之间的随机浮点数
print(random.random())
# 重新设置一样的 seed，生成的随机数将是同一个
# 默认的 seed 是操作系统当前时间
# random.seed(1)
print(random.random())

# randint() - 生成指定范围内的随机整数
print("======================= randint() =======================")
print(random.randint(1, 10))
print(random.randint(1, 100))

# choice() - 从序列中随机选取一个元素
print("======================= choice() =======================")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(numbers))
print(random.choice(numbers))
print(random.choice(numbers))

# shuffle() - 将序列中的元素随机排序
print("======================= shuffle() =======================")
random.shuffle(numbers)
print(numbers)

random.shuffle(numbers)
print(numbers)

random.shuffle(numbers)
print(numbers)

# samples() - 从序列中随机选取指定数量的元素
print("======================= samples() =======================")
print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 4))

# uniform() - 生成指定范围内的随机浮点数
print("======================= uniform() =======================")
print(random.uniform(1, 5))
print(random.uniform(1, 10))
print(random.uniform(1, 50))
print(random.uniform(1, 100))
