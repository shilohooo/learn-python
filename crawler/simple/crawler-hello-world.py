"""
爬虫基础

@author: shiloh
@date: 2025/3/7 16:56
"""
import json
from urllib import request as sys_req_lib
import requests

headers = {
    # 假装是浏览器，否则可能会被拒绝访问
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Content-Type': 'application/json;charset=utf-8'
}
# req = sys_req_lib.Request('https://www.baidu.com', headers=headers)
# resp = sys_req_lib.urlopen(req)
# print(resp.read().decode('utf-8'))

# data = {
#     "name": "username",
#     "password": "pwd",
#     "codeId": "uuid",
#     "verifyCode": "verifyCode"
# }
# login_req = request.Request('login-api-url',
#                             data=bytes(json.dumps(data), 'utf-8'), headers=headers)
# login_resp = request.urlopen(login_req)
# print(json.loads(login_resp.read().decode('utf-8')))
params = {
    'searchVal': 'python'
}
data = {
    'name': 'username',
}
resp = requests.get('https://www.baidu.com', headers=headers, params=params, json=data, verify=False, timeout=3.0)
# print(resp.status_code)
# print(resp.headers)
# print(resp.text)
print(resp.cookies)
for item in resp.cookies.items():
    print(item)
print(resp.cookies['BAIDUID'])
