"""
python - 使用 json 数据结构存储数据
Python 中使用 json.dump() 和 json.load() 来存储和读取 json 文件。
"""
import json

# 首先要导入 json 模块

# 创建测试数据
user_info = {'name': 'shiloh', 'age': 26, 'gender': 'male'}

# 将 json 数据写入到文件中
json_file_path = 'user-info.json'
with open(json_file_path, 'w') as writer:
    json.dump(user_info, writer)

# 读取 json 文件中的内容
with open(json_file_path) as reader:
    content = json.load(reader)
    print(content)
