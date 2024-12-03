"""
python 标准库 - Copy
Copy 模块包含了一组用来复制列表、对象、数组等不同元素的函数
分浅拷贝和深拷贝
"""
import copy

# 浅拷贝
a = [[1], [2], [3]]
b = copy.copy(a)
a[0][0] = 4
print(a)
print(b)

# 深拷贝
c = copy.deepcopy(a)
a[0][0] = 0
a[1] = None
print(a)
print(c)
