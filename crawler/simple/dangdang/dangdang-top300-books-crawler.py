"""
当当网好评榜TOP300书籍信息爬虫

@author: shiloh
@date: 2025/3/8 10:33
"""
import json

import requests
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}


def send_request_by_page(url):
    """
    发生请求获取网页内容
    :param url: 请求地址，每次的页数不一样
    :return: 网页内容
    """
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code == 200:
            return resp.text
    except requests.RequestException as e:
        print(f'请求失败，错误信息为{e}')
        return None


def parse_response(html):
    """
    解析HTML响应，提取书籍信息。

    该函数使用正则表达式匹配HTML中的书籍信息，包括书籍排名、图片、标题、推荐人数、作者、获奖次数和价格。

    正则表达式详细说明：

    - '<li>.*?list_num.*?(\d+).' 匹配书籍排名

    - '<img src="(.*?)"' 匹配书籍图片URL

    - 'class="name".*?title="(.*?)"' 匹配书籍标题

    - 'class="tuijian">(.*?)</span>' 匹配推荐人数

    - 'class="publisher_info">.*?target="_blank">(.*?)</a>' 匹配作者信息

    - 'class="biaosheng">.*?<span>(.*?)</span>' 匹配获奖次数

    - '<span class="price_n">&yen;(.*?)</span>' 匹配书籍价格

    :param html: 网页的HTML内容
    :type html: str
    :return: 生成器，迭代返回每本书籍的信息字典
    :rtype: list[dict[str, str]]
    """
    # 编译正则表达式，用于匹配HTML中书籍的相关信息
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)

    # 使用正则表达式查找所有匹配的书籍信息
    items = re.findall(pattern, html)

    # 遍历所有匹配的书籍信息，yield返回每本书籍的信息字典
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def write_items_to_file(items):
    """
    将图书信息以JSON字符串的形式写入到文件中

    :param items: 图书信息字典列表
    :type items: list[dict[str, str]]
    """
    for item in items:
        print(f'开始写入数据========》{item}')
        with open('dangdang-top300-books.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
            f.close()


def main(page):
    url = f'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{page}'
    html = send_request_by_page(url)
    items = parse_response(html)
    write_items_to_file(items)


if __name__ == '__main__':
    for i in range(1, 16):
        main(i)
