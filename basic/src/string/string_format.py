"""
python 字符串格式化
str.format()
"""
from datetime import datetime
from string import Template

name = "shiloh"
age = 26
print("Hello I am {}, my age is {}".format(name.title(), age))

# Python3.6+ 以后，推荐使用 f-string
# f-string 以 f 或者 F 开头
print(f"Hello my name is {name.title()}, I am {age} years old.")
# f-string 还可以包含表达式
a = 5
b = 10
print(F"{a} + {b} = {a + b}")

# 多行 f-strings
print(
    f"Hi, I am {name.upper()}"
    f"I am {age} years old."
)

# = 符号在 f-string 中的使用
now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
# {now=} 将输出表达式和它的值，表达式为 now=，值为变量 now 的值
print(f"date and time: {now=}")

# 添加空格或符号
# -^20 表示变量的值居中，左右使用 - 符号填充，直到字符长度满足20个字符
print(f"{name.upper() = :-^20}")
# 不指定符号，则使用空格填充
print(f"{name.upper() = :^20}")
# 不指定 ^ ，则在变量值后面填充
print(f"{name.upper() = :20}")

# 数字格式化
a = 1000_0000
# 保留小数点后两位
print(f"{a:.2f}")
# 四舍五入
pi = 3.1415926
print(f"{pi:.2f}")

# 格式化为百分比，并保留两位小数，四舍五入
percent = 0.816562
print(f"{percent:.2%}")

# 模板字符串
t = Template("Hey $name!")
print(t.substitute(name=name))
