"""
python - 文件写入
"""

# 覆盖写入
file_path = 'test.txt'
# open()函数第一个参数为文件路径，第二个参数 mode 为模式
# w 代表写入模式，mode 参数的默认为 r，也就是读取模式
# 可选的模式有：
# r = 只读
# w = 只写，如果文件不存在则新建一个，如果文件存在则先清空文件内容再写入
# a = 附加模式，写入的内容追加到原始文件后面，文件不存在也会创建
# r+ = 可读可写（覆盖）模式
# a+ = 可读可写（追加）模式
# with open(file_path, 'w') as file_obj:
#     file_obj.write('I ❤ Python\n')
#
# # 追加写入
# with open(file_path, 'a') as file_obj:
#     file_obj.write('I ❤ Python\n')
#
# # 打印文件内容
# with open(file_path) as file_obj:
#     print(file_obj.read().rstrip())

with open(file_path, 'a+') as file:
    file.write('I love python\n')
    # 写入文件后，指针会移动到文件末尾
    # 如果想在写入后立即读取文件内容，需要将指针移动到文件开头
    file.seek(0)
    content = file.read()
    print(content.rstrip())
