"""
python 字典推导式/解析式
"""

user_info = {"name": "shiloh", "age": 26, "gender": "male"}
# 反转 key value
k_v_reverse = {v: k for k, v in user_info.items()}
print(k_v_reverse)
