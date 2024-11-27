"""
python 日志打印

日志等级：
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

# 导入日志模块
import logging

# 日志配置
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# 输入日志到日志文件中
logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Program starting...')
name = 'shiloh'
logging.debug('Username is %s', name)
num = 5
logging.debug('Program exit...%s' % num)

# 禁用某个级别的日志
logging.disable(logging.DEBUG)
logging.debug("debug log")
logging.info("info log")
logging.error("error log")
