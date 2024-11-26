"""
python 文件路径操作 - os.path
"""

# shutil 模块提供了复制文件、目录的函数
import os
import shutil

TEST_FILE_PATH = "./test.txt"

#  路径拼接
print(os.path.join("usr", "bin", "spam"))

my_files = ["a.txt", "b.txt", "c.txt"]
dir_name = "C:\\Users\\shiloh\\code"
for filename in my_files:
    print(os.path.join(dir_name, filename))

# 获取当前工作路径
print(os.getcwd())

# 切换当前工作路径
# os.chdir(dir_name)
# print(os.getcwd())

# 创建新目录
# os.makedirs(f"{dir_name}\\test_dir")

# 绝对路径和相对路径
# 绝对路径总是以根路径开始
# 相对路径是相对于程序当前工作路径
# . 代表当前目录，.. 代表上级目录

# 判断是否为绝对路径
print(os.path.isabs("C://"))
print(os.path.isabs("./"))

# 获取当前所在目录的绝对路径
print(os.getcwd())

# 获取上级目录的绝对路径
print(os.path.abspath(".."))

# 获取相对路径：指定A路径、获取它相对于B路径的相对路径
TEST_DIR_PATH = "C:\\Users"
print(os.path.relpath(TEST_DIR_PATH, "C:\\"))

# 文件/路径检查 - 检查文件/路径是否存在
print(os.path.exists("."))
print(os.path.exists("./non_existent_file.py"))

# 检查路径是否为文件
print(os.path.isfile(TEST_DIR_PATH))
print(os.path.isfile(TEST_FILE_PATH))
print(os.path.isfile("./non_existent_file.py"))

# 检查路径是否为目录
print(os.path.isdir(TEST_DIR_PATH))
print(os.path.isdir(TEST_FILE_PATH))

# 获取文件大小，单位：bytes
print(f"文件：{TEST_FILE_PATH} 大小为：{os.path.getsize(TEST_FILE_PATH)} 字节")

# 列出指定目录下面的所有文件/子目录
print(os.listdir(TEST_DIR_PATH))
for f in os.listdir(TEST_DIR_PATH):
    # 输出的仅是文件名/子目录名
    print(f)

# 计算指定目录下的文件大小
total_size = 0
for filename in os.listdir(TEST_DIR_PATH):
    total_size += os.path.getsize(os.path.join(TEST_DIR_PATH, filename))

print(f"{total_size=}")

# 复制文件和目录
shutil.copy(TEST_FILE_PATH, TEST_DIR_PATH)
# 复制整个目录以及该目录下的所有文件
shutil.copytree("./test", os.path.join(TEST_DIR_PATH, "test"))

# https://www.pythoncheatsheet.org/cheatsheet/file-directory-path#moving-and-renaming
