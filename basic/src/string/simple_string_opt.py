# 字符串的简单运算

name = "cool coder"
print(name)
# title() - 以首字母大写的方式显示每个单词
print(name.title())
# upper() - 全部大写
print(name.upper())
# lower() - 全部小写
print(name.lower())

# 字符串拼接
first_name = "bruce"
last_name = 'lee'
full_name = first_name + ' ' + last_name
print(full_name)

# 转义字符 - 制表符
print("\ttest")
# 转义字符 - 换行符
print('hello\nworld')

msg = ' python '
print(msg)
# 删除多余空格 - 删除右侧的空格
print(msg.rstrip())
# 删除多余空格 - 删除左侧的空格
print(msg.lstrip())
# 删除多余空格 - 删除两侧的空格
print(msg.strip())