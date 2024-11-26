"""
python 文件路径操作 - pathlib
pathlib 是 python3.4 新增的，提供以面向对象的方式操作文件系统路径
"""

from pathlib2 import Path

TEST_FILE_PATH = "./test.txt"

TEST_DIR_PATH = "C:\\Users\\shiloh"

#  路径拼接，python 会自动处理不同平台上的文件路径分隔符
print(Path("usr") / "bin" / "spam")

my_files = ["a.txt", "b.txt", "c.txt"]
home = Path.home()
for filename in my_files:
    print(home / filename)

# 获取当前工作路径
print(Path.cwd())
# 修改当前工作路径
# os.chdir("C:\\Users\\shiloh\\code")
# print(Path.cwd())

# 创建新目录
# cwd = Path.cwd()
# mkdir(parents=True) 当父目录不存在时，会自动创建
# (cwd / "test_dir" / "sub_dir").mkdir(parents=True)

# 绝对路径和相对路径
# 绝对路径总是以根路径开始
# 相对路径是相对于程序当前工作路径
# . 代表当前目录，.. 代表上级目录

# 判断是否为绝对路径
print(Path("C:\\").is_absolute())
print(Path("..").is_absolute())

# 获取当前所在目录的绝对路径
print(Path.cwd())

# 获取上级目录的绝对路径
print(Path("..").resolve())

# 获取相对路径：指定A路径、获取它相对于B路径的相对路径
print(Path(TEST_DIR_PATH).relative_to("C:\\"))

# 文件/路径检查 - 检查文件/路径是否存在
print(Path(".").exists())
print(Path("./non_existent_file.py").exists())

# 检查路径是否为文件
print(Path(TEST_DIR_PATH).is_file())
print(Path(TEST_FILE_PATH).is_file())
print(Path("./non_existent_file.py").is_file())

# 检查路径是否为目录
print(Path(TEST_DIR_PATH).is_dir())
print(Path(TEST_FILE_PATH).is_dir())

# 获取文件大小，单位：bytes
stat = Path(TEST_FILE_PATH).stat()
print(stat)
print(stat.st_size)

# 列出指定目录下面的所有文件/子目录
for f in Path(TEST_DIR_PATH).iterdir():
    # 输出的是文件/子目录的绝对路径
    print(f)

# 计算指定目录下的文件大小
total_size = 0
for sub_path in Path(TEST_DIR_PATH).iterdir():
    total_size += sub_path.stat().st_size

print(f"{total_size=}")
