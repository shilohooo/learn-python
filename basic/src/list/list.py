# 列表用方括号 [] 标识，用逗号分隔其中的元素
fruits = ["apple", "banana", "orange"]
# 在末尾添加元素
fruits.append("watermelon")
# 打印列表
print(fruits)

# 通过 [index] 下标访问列表中的元素，从 0 开始
print(fruits[0])
print(fruits[2])
# 获取列表中的最后一个元素，可以使用 [-1] 下标，倒数第二个元素则是 [-2]
print(fruits[-1])

# 通过索引修改元素
fruits[0] = "grape"
print(fruits[0])

# 在指定位置插入元素
fruits.insert(1, "apple")
print(fruits)

# 删除元素

# 第一种方式：del list[index] - 按索引删除
del fruits[0]
print(fruits)

# 第二种方式：list.pop() - 删除列表中的最后一个元素，也可以传索引来删除指定位置的元素
# pop() 弹出元素，带返回值
# fruits.pop()
deleted_fruit = fruits.pop(2)
print("delete fruit is:" + deleted_fruit)
print(fruits)

# 第三种方式：remove() - 根据元素值删除元素
fruits.remove("apple")
print(fruits)

# 列表排序
nums = [3, 2, 4, 6, 5, 1]
print(nums)
# 主要有两种方式：
# 1.使用 sort() 方法对列表进行永久性排序
# sort() 会改变原列表
# nums.sort()
# print(nums)
# 如果要倒着排，可以给 sort() 方法传递参数 reverse = true
# nums.sort(reverse=True)
# print(nums)
# 2.使用 sorted() 方法对列表进行临时排序
# sorted() 方法不会改变原列表，而是返回一个排序后的新列表
# print(sorted(nums))
# print(sorted(nums, reverse=True))

# 反转列表：reverse()，该方法会改变原来的列表
# 需要注意的是，reverse() 只会按原来的顺序进行反转，它不是排序
nums.reverse()
print(nums)

# 获取列表的长度（列表中有多少个元素）
length = len(nums)
print("列表中有" + str(length) + "个元素")

# 遍历列表
# 使用 for...in 循环
for num in nums:
    print(num)

print("===============================")

# range() 函数，生成一系列数字，包含起始值，排除结束值
# 这里打印的是 1 - 9
for val in range(1, 10):
    print(val)

print("===============================")

# 还可以指定步长，即每次增长2
for val in range(1, 10, 2):
    print(val)

print("===============================")

# 对列表的简单计算
# 1. 计算列表中的最小值 - min()
print("列表中的最小值为：" + str(min(nums)))
# 2. 计算列表中的最小值 - max()
print("列表中的最大值为：" + str(max(nums)))
# 3. 计算列表中的值的总和 - sum()
print("列表中的值的综合为：" + str(sum(nums)))

# 列表解析：求列表中的每个元素的平方，然后放到一个新的列表中
# 语法：variable = [expression for...in]
# 下面这行代码为计算列表中的每个数字的平方，然后生成新的列表
squares = [x**2 for x in range(1, 11)]
print(squares)

# 列表切片
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，Python在到达你指定的第二个索引前面的元素后停止。
# 要输出列表中的前三个元素，需要指定索引0~3
names = ["shiloh", "bruce", "jack", "rose", "tom"]
# 从第二个元素开始输出，一直输出到第四个
print(names[1:4])
# 如果你没有指定第一个索引，Python将自动从列表开头开始：从第一个元素开始输出，一直输出到第四个
print(names[:4])
# 如果没有指定终止的索引，将自动取到列表末尾：从第二个元素开始输出，一直到末尾
print(names[1:])
# 使用负数，表示从末尾开始取：返回最后三个元素
print(names[-3:])
# 遍历切片
for name in names[1:3]:
    print(name)

# 通过切片来快速复制列表
names_clone = names[:]
print(names_clone)
# 通过切片复制出来的列表是一个全新的列表，改变它不会影响原来的列表
print("update clone list")
names_clone[1] = "thomas"
print(names)
print(names_clone)
# 如果简单的通过赋值来创建新的列表，那么两个列表实际同时指向的是同一个，改变其中一个就会影响到另外一个
print("list assignment")
names2 = names
names2[1] = "peter"
print(names)
print(names2)
