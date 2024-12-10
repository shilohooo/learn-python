"""
python 标准库 - datetime：日期时间操作
该模块提供了三个关于日期的数据类型：
1.date
2.time
3.datetime
"""
import datetime
from datetime import timedelta

# date：获取包含年、月、日属性的日期对象
date_obj = datetime.date(2024, 12, 3)
# 输出格式：%Y-%m-%d
print(date_obj)
# 获取年、月、日属性
# 年份 1 - 9999
print(date_obj.year)
# 月份 1 - 12
print(date_obj.month)
# 日期 1 - 31
print(date_obj.day)

# time：获取包含时、分、秒、微妙、时区信息属性的时间对象
time_obj = datetime.time(16, 44, 14)
# 输出格式：%H:%M:%S
print(time_obj)
# 小时 0 - 23
print(time_obj.hour)
# 分钟 0 - 59
print(time_obj.minute)
# 秒 0 - 59
print(time_obj.second)
# 微妙 0 - 999999
print(time_obj.microsecond)

# 日期时间：包含 date、time 对象的属性
datetime_obj = datetime.datetime(2024, 12, 3, 16, 48, 39)
# 输出格式：%Y-%m-%d %H:%M:%S
print(datetime_obj)
print(datetime_obj.year)
print(datetime_obj.month)
print(datetime_obj.day)
print(datetime_obj.hour)
print(datetime_obj.minute)
print(datetime_obj.second)
print(datetime_obj.microsecond)

# 获取当前日期时间，格式：yyyy-MM-dd HH:mm:ss:SSS
# datetime.now()、datetime.today() 返回的对象都包含了 date、time 对象的属性
# now() 还可以设置时区，比如设置为东八区
# 如果没有设置时区，将使用系统默认时区
now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
print(now)
print(now.year)
print(now.hour)
# 第二种方式
today = datetime.datetime.today()
print(today)

# 日期、时间格式化、解析
# 格式参考：https://www.pythoncheatsheet.org/modules/datetime-module#strftime-and-strptime
# strftime() - 格式化日期、时间
# 只输出日期
print(now.strftime("%Y-%m-%d"))
# 只输出时间
print(now.strftime("%H:%M:%S"))

# 解析时间
date_str = "1998-03-02"
formatted_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
# 格式化日期，但没有指定时间，时间会被自动设置为 00:00:00
print(formatted_date)

time_str = "17:30:05"
formatted_time = datetime.datetime.strptime(time_str, "%H:%M:%S")
# 格式化时间，但没有指定日期，日期会被自动设置为 1900-01-01
print(formatted_time)

datetime_str = "1998-03-02 00:05:23"
formatted_datetime = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
print(formatted_datetime)

# timedelta() - 获取两个日期之间的时间差
date1 = datetime.date(2024, 12, 1)
date2 = datetime.date(2024, 12, 3)
diff = date2 - date1
print(diff)
# 相差多少天
print(diff.days)

# timedelta() 可以添加日期、秒、毫秒到一个 datetime 对象
current_time = datetime.datetime.now()
print(f"{current_time=}")
print(current_time + timedelta(days=1, seconds=60))

# 也可以减少日期、秒、毫秒
print(current_time - timedelta(days=2))
