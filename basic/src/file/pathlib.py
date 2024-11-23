"""
python 文件路径操作 - pathlib
pathlib 是 python3.4 新增的，提供以面向对象的方式操作文件系统路径
"""
import os

from pathlib import Path

#  路径拼接，python 会自动处理不同平台上的文件路径分隔符
print(Path("usr") / "bin" / "spam")

my_files = ["a.txt", "b.txt", "c.txt"]
home = Path.home()
for filename in my_files:
    print(home / filename)

# 获取当前工作路径
print(Path.cwd())
# 修改当前工作路径
os.chdir("D:\\shiloh\\develop")
print(Path.cwd())

# 创建新目录
cwd = Path.cwd()
# mkdir(parents=True) 当父目录不存在时，会自动创建
(cwd / "test_dir" / "sub_dir").mkdir(parents=True)
