"""
python - 文件操作
要使用文本文件中的信息，首先需要将信息读取到内存中。
为此，你可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取。
"""

# 读取整个文件内容为字符串
# open() 函数用于打开一个文件，参数为文件路径，可以是相对路径或者绝对路径
# 关键字 with 在不再需要访问文件后将其关闭，节省资源，可以理解为 Java 的 try-with-resources
with open('test.txt') as file_obj:
    content = file_obj.read()
    print(content)

# 逐行读取文件内容
with open('test.txt') as file_obj:
    # 以循环的方式来获取每一行的内容
    for line in file_obj:
        # read() 方法在读取到文件末尾时，返回一个空字符串
        # 因此，读取到的文件内容，会比实际的内容多了一个空行
        # 使用 rstrip() 删除多余的空行
        print(line.rstrip())
