# 浮点数

# 只需输入要使用的数字，Python通常都会按你期望的方式处理它们
print(0.1 + 0.1)
print(0.2 * 0.4)
print(2 * 0.1)
print(2 * 0.2)
# 注意：小数位数可能是不确定的
print(0.2 + 0.1)
print(3 * 0.1)

# 数字与字符串拼接
num = 1
msg = ' hello'
# 下面这行代码会出现警告，因为类型不兼容
# print(num + msg)
# 需要使用 str() 函数来将数字转换为字符串，避免类型错误
print(str(num) + msg)

age = 26
print('my age is ' + str(age))