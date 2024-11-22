"""
爬虫入门：B站热搜数据爬虫
"""

import matplotlib.pyplot as plt
import requests
import wordcloud

# 热搜数据接口地址
api_url = "https://api.bilibili.com/x/web-interface/wbi/search/square"
params = {
    "limit": 10,
    "platform": "web",
    "w_rid": "d476b6d35e5ef9047012c6b562561d1f",
    # "wts": time.time()
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Content-Type": "application/json;charset=utf-8"
}
print(f"{params=}")

# 发请求
response = requests.get(api_url, params=params, headers=headers)
print(response)
print(f"{response.url=}")
print(f"{response.status_code=}")
# 解析响应数据
resData = response.json()
hot_search_list = resData["data"]["trending"]["list"]
# hot_search_keywords = []
# key = word, value = 词频
hot_search_keywords_freq = {}
for item in hot_search_list:
    print(f"热搜词：{item['keyword']}")
    # hot_search_keywords.append(item["keyword"])
    keyword = item["keyword"]
    hot_search_keywords_freq[keyword] = item["heat_score"]

# print(hot_search_keywords)
print(hot_search_keywords_freq)

# 生成词云
word_cloud = wordcloud.WordCloud(
    height=600,
    width=400,
    background_color="white",
    # 中文字体文件，防止乱码
    font_path="msyh.ttc"
)
# word_cloud.generate(" ".join(hot_search_keywords))
# 按词频生成，词频越大字体越大
word_cloud.generate_from_frequencies(hot_search_keywords_freq)
# 输出图片到本地文件夹
word_cloud.to_file("bilibili_hot_search_wordcloud.png")

# 显示图像
# interpolation='bilinear' 表示插值方法为双线性插值
plt.imshow(word_cloud, interpolation="bilinear")
# 关闭坐标
plt.axis("off")
plt.show()
