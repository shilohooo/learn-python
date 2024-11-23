"""
python 文件路径操作 - os.path
"""

import os

#  路径拼接
print(os.path.join("usr", "bin", "spam"))

my_files = ["a.txt", "b.txt", "c.txt"]
dir_name = "D:\\shiloh\\develop"
for filename in my_files:
    print(os.path.join(dir_name, filename))

# 获取当前工作路径
print(os.getcwd())

# 切换当前工作路径
os.chdir(dir_name)
print(os.getcwd())

# 创建新目录
os.makedirs(f"{dir_name}\\test_dir")
