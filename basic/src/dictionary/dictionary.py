"""
python 中的字典
在Python中，字典是一系列键-值对。每个键都与一个值相关联，
你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。
事实上，可将任何Python对象用作字典中的值。
"""

# 字段 CRUD
# 在Python中，字典用放在花括号{}中的一系列键-值对表示。
user = {"name": "Shiloh595", "age": 16, "gender": "male", "sex": "male"}
print(user)
# 通过 key 访问字典中的值
name = user["name"]
print("user name: " + name)
# 添加键值对
user["email"] = "shiloh595@gmail.com"
print(user)
# 修改字典中的值
user["age"] = 24
print(user)
# 删除字典中的键值对
del user["email"]
print(user)

# 遍历字典：字典可用于以各种方式存储信息，因此有多种遍历字典的方式：可遍历字典的所有键—值对、键或值。
# 遍历所有的键值对
# 注意：即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。
print(
    "====> print all key value pairs <===="
)
for k, v in user.items():
    print(k + ": " + str(v))

print("====> print all keys <====")
# 遍历所有的键
for k in user.keys():
    print(k.title())
# 遍历字典时，默认遍历的就是所有的 key
for k in user:
    print(k)

# 按顺序遍历所有的 key
print(
    "====> print all keys after sorted <===="
)
for k in sorted(user.keys()):
    print(k)

print("====> print all values <====")
# 遍历所有的值
for v in user.values():
    print(v)

print(
    "====> print all values after remove duplicate values <===="
)
# 去除重复的值
for val in set(user.values()):
    print(val)
