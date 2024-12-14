"""
python 标准库 - os

用于调用依赖操作系统的功能
"""

import os

# 路径拼接，自动根据当前操作系统区分路径分隔符
print(os.path.join("a", "b", "c"))
files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in files:
    print(os.path.join("D:\\", filename))

# 当前工作目录
print(os.getcwd())
# 修改当前工作目录
# os.chdir("D:\\")
# print(os.getcwd())
# 创建新目录
# os.makedirs("D:\\test\\nested")

# 绝对路径操作
print(os.path.isabs("D:\\"))
print(os.path.isabs(".."))
print(os.path.isabs("."))

# 获取绝对路径
print(os.path.abspath(".."))

# 相对路径操作
print(os.path.relpath("D:\\test\\nested", "D:\\"))

# 目录/文件校验
# 判断目录/文件是否存在
print(os.path.exists("."))
print(os.path.exists("a.py"))
print(os.path.exists("D:\\test1"))
# 判断给定路径是否为文件，不存在的文件判断结果也为 False
print(os.path.isfile("."))
print(os.path.isfile("os-example.py"))
print(os.path.isfile("non_existent_file.py"))
# 判断给定路径是否为目录
print(os.path.isdir("."))
print(os.path.isdir(".."))
print(os.path.isdir("os-example.py"))
# 不存在的目录判断结果也为 False
print(os.path.isdir("D:\\non_existent_dir"))

# 获取文件大小，单位：bytes
print(os.path.getsize("../json/user-info.json"))

# 列出指定目录下面的所有文件/子目录
print(os.listdir(".."))

# 计算某个目录下面所有文件的大小
total_size = 0
for filename in os.listdir(".."):
    total_size += os.path.getsize(os.path.join("..", filename))

print(total_size)

# 删除文件或目录（目录里面不能有任何文件或子目录）
os.unlink("./delete-me.txt")
os.rmdir("D:\\test\\nested")
