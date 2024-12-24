"""
爬虫：豆瓣电影TOP250排行榜

@author: shiloh
@date: 2024/12/23 16:09
"""
import re
from time import sleep

import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {
    # 伪装成浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'cookie': 'bid=47GW4LeeyQY; _pk_id.100001.4cf6=cfc8c9057f9277fc.1734940617.; ll="118286"; _vwo_uuid_v2=DFA415450A2114F634585374FAA05F078|ba8c7a99500b39f51ab9bff348b41c53; dbcl2="227337760:HLoGG6atpHE"; __utmz=30149280.1734943977.2.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1734943977.2.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; ck=XTyY; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1735032803%2C%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.889669202.1734940617.1734943977.1735032803.3; __utmb=30149280.0.10.1735032803; __utmc=30149280; __utma=223695111.933700798.1734940617.1734943977.1735032803.3; __utmb=223695111.0.10.1735032803; __utmc=223695111'
}
total_movies = 250
page_size = 25


def get_movies():
    """
    爬取豆瓣电影TOP250排行榜
    :return:
    """

    movies = []
    for start in range(0, total_movies + 1, page_size):
        params = {
            'start': start
        }
        resp = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(resp.text, 'html.parser')
        movie_elements = soup.find('ol', class_='grid_view')
        movie = {}
        for movie_item in movie_elements.find_all('div', class_='item'):
            try:
                # 封面图片地址
                movie['cover_src'] = movie_item.find('img')['src']
                # 电影名称（TODO：可能有多个）
                movie['title'] = movie_item.find('span', class_='title').text
                # 评分信息
                star_div = movie_item.find('div', class_='star')
                # 评分分值
                movie['rating'] = star_div.find('span', class_='rating_num').text
                # 评价人数
                movie['total_raters']: str = re.sub(r'\D', "", list(star_div.children)[-2].text)
                # 概况
                movie['overview'] = movie_item.find('span', class_='inq').text
                # 相关内容
                movie['bd']: str = movie_item.find('div', class_='bd').find('p').text.strip().replace('/', "").replace(
                    '\xa0', "")
                movies.append(movie)
            except AttributeError as e:
                print(e)

        # 休息 3 秒，避免被封IP
        sleep(3.0)

    return movies


if __name__ == '__main__':
    movies = get_movies()
    print(movies)
