"""
python 标准库 - shelve

类似字典的一个持久化对象，key 为普通字符串，值则可以存储任意的 python 对象
底层依赖于 SQLite
"""

import shelve

# 存储
wife = ['Pretty', 'Lovely', 'Nice']
with shelve.open('mydata') as shelf_file:
    shelf_file['wife'] = wife

# 读取
with shelve.open('mydata') as shelf_file:
    # 跟字典一样，shelf 的值也有 keys() 和 values() 方法
    # 用于获取 key 和 value 的类列表数据，如果要使用这些返回值
    # 可以使用 list() 或者 tuple() 将其转换为列表或者元组
    print(list(shelf_file.keys()))
    print(list(shelf_file.values()))
    print(type(shelf_file))
    print(shelf_file['wife'])
