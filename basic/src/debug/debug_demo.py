"""
python debug demo

查找和解决 bug
"""
import traceback

# 抛出异常
try:
    raise Exception('抛出异常')
except:
    # 获取堆栈信息，写入到错误日志中，指定编码避免中文乱码
    with open('error_log.log', 'w', encoding='utf-8') as err_file:
        # write() 的返回值为写入的字节数
        wrote_bytes = err_file.write(traceback.format_exc())
        print(f'异常信息已保存到错误日志中~{wrote_bytes=}')

# 断言
name = 'shiloh123'
# 断言如果返回 False，将抛出 AssertionError 异常
# 在允许 python 代码时，可以加上 -o 选项来禁用断言
try:
    assert name == 'shiloh', '用户姓名不是 shiloh'
except AssertionError as e:
    print(traceback.format_exc())
