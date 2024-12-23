"""
爬虫：豆瓣电影TOP250排行榜

@author: shiloh
@date: 2024/12/23 16:09
"""
import re
from time import sleep

import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250"
headers = {
    # 伪装成浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'cookie': 'bid=47GW4LeeyQY; ap_v=0,6.0; _pk_id.100001.4cf6=cfc8c9057f9277fc.1734940617.; __utmc=30149280; __utmc=223695111; ll="118286"; _vwo_uuid_v2=DFA415450A2114F634585374FAA05F078|ba8c7a99500b39f51ab9bff348b41c53; dbcl2="227337760:HLoGG6atpHE"; ck=XTyY; __utma=30149280.889669202.1734940617.1734940617.1734943977.2; __utmb=30149280.0.10.1734943977; __utmz=30149280.1734943977.2.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.933700798.1734940617.1734940617.1734943977.2; __utmb=223695111.0.10.1734943977; __utmz=223695111.1734943977.2.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1734943977%2C%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%5D; _pk_ses.100001.4cf6=1; push_noty_num=0; push_doumail_num=0'
}
total_movies = 250
page_size = 25


def get_movies():
    """
    爬取豆瓣电影TOP250排行榜
    :return:
    """

    for start in range(0, total_movies + 1, page_size):
        params = {
            "start": start
        }
        resp = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(resp.text, "html.parser")
        movies = soup.find("ol", class_="grid_view")
        for movie_item in movies.find_all("div", class_="item"):
            # 封面图片地址
            cover_src = movie_item.find("img")['src']
            # 电影名称（TODO：可能有多个）
            title = movie_item.find("span", class_="title").text
            # 评分信息
            star_div = movie_item.find("div", class_="star")
            # 评分分值
            rating = star_div.find("span", class_="rating_num").text
            # 评价人数
            total_raters: str = re.sub(r"\D", "", list(star_div.children)[-2].text)
            # 概况
            overview = movie_item.find("span", class_="inq").text
            # 相关内容
            bd: str = movie_item.find("div", class_="bd").find("p").text.strip().replace("/", "").replace("\xa0", "")

            print("=============================== movie info ===============================")
            print(f"{cover_src=}")
            print(f"{title=}")
            print(f"{rating=}")
            print(f"{total_raters=}")
            print(f"{overview=}")
            print(f"{bd=}")
            print("=============================== movie info ===============================")
            print()

        # sleep(3.0)
        break


if __name__ == '__main__':
    get_movies()
