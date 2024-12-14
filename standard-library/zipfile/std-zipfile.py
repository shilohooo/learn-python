"""
python 标准库 - zipfile

该模块提供了创建、读取、写入、列出压缩文件的工具
"""
import datetime
import zipfile

# 读取压缩文件
with zipfile.ZipFile('test.zip') as zip_reader:
    # 列出压缩包里面有哪些文件，包括子目录
    print(zip_reader.namelist())
    # 获取压缩包里面的某个文件信息
    file_info = zip_reader.getinfo('test/a.txt')
    # 文件大小
    print(file_info.file_size)
    # 文件压缩后的大小
    print(file_info.compress_size)
    # 计算出压缩之后文件大小缩小了多少倍
    print(f'Compressed file is {(round(file_info.file_size / file_info.compress_size, 2))}x smaller!')

# 压缩文件提取
# 将压缩包内的所有文件和目录解压到当前工作目录
# with zipfile.ZipFile('test.zip') as reader:
#     reader.extractall()

# 将压缩包内指定的单个文件解压到当前工作目录
# with zipfile.ZipFile('test.zip') as reader:
#     print(reader.extract('test/a.txt'))
# 解压到指定的目录
# print(reader.extract('test/a.txt', 'D:\\'))

# 创建压缩包 & 添加文件到压缩包
# with zipfile.ZipFile('new.zip', 'w') as writer:
#     writer.write('a.txt', compress_type=zipfile.ZIP_DEFLATED)

# 读取压缩包的元数据
with zipfile.ZipFile('test.zip') as reader:
    for info in reader.infolist():
        system = 'Windows' if info.create_system == 0 else 'Unix'
        # *variable 用于解构可迭代对象，如元组、列表
        modified = datetime.datetime(*info.date_time)
        print("===================== file info ======================")
        print(f"Filename:\t{info.filename}")
        print(f"Comment:\t{info.comment}")
        print(f"Modified:\t{modified}")
        print(f"System:\t{system}")
        print(f"ZIP Version:\t{info.create_version}")
        print(f"Compressed:\t{info.compress_size} bytes")
        print(f"Uncompressed:\t{info.file_size} bytes")
        print("===================== file info ======================")
        print()
