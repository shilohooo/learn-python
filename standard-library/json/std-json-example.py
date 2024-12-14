"""
python json 标准库
"""

import json

# JSON loads() 方法 - 将 JSON 字符串转换为 python 对象，该过程称之为反序列化
person_json_str = '{"name": "Charles", "age": 33, "has_hair": false, "hobbies": ["photography", "running"]}'
# json to python object
person_obj = json.loads(person_json_str)
print(person_obj)
# json 对象转换后是字典类型
print(type(person_obj))
print(f"person name: {person_obj.get("name")}")

# JSON dumps() 方法 - 将 python 对象转换为 JSON 数据，该过程成为序列化
person_json = json.dumps(person_obj)
print(person_json)
# 转换后类型为字符串
print(type(person_json))

# 读取和写入 JSON 文件
# 读
with open('test.json') as reader:
    json_content = json.loads(reader.read())
    print(json_content)

# 写入
user = {
    'name': 'shiloh',
    'age': 26,
    'email': 'shiloh595@gmail.com',
    "enabled": True
}

with open('user-info.json', 'w') as writer:
    writer.write(json.dumps(user))
