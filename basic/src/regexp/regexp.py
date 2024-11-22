"""
python 正则表达式
"""

# 导入正则表达式模块
import re

# 创建正则表达式对象，注意要传递 raw string 作为参数
pattern = re.compile(r"1[358]\d{9}")
# 匹配
search_str = "My phone number is 13025715370"
match = pattern.search(search_str)
# 获取匹配的内容
print(match.group())

# 通过括号分组捕获
phone_num_regexp = re.compile(r"(\d{4})-(\d{7})")
content = "My landline is 0752-6629395"
result = phone_num_regexp.search(content)
print("========================= group(1) =========================")
print(result.group(1))
print("========================= group(2) =========================")
print(result.group(2))
print("========================= group(0) =========================")
print(result.group(0))
print("========================= group() =========================")
print(result.group())
# 一次性接收捕获到的所有分组
print("========================= groups() =========================")
print(result.groups())
area_code, main_number = result.groups()
print(f"{area_code=}")
print(f"{main_number=}")

# 管道符
print("========================= Pipe =========================")
hero_regexp = re.compile(r"Batman|Tina Fey")
match_hero = hero_regexp.search("Batman and Tina Fey.")
# 输出 Batman
print(match_hero.group())
match_hero2 = hero_regexp.search("Tina Fey and Batman.")
# 输出 Tina Fey
print(match_hero2.group())
