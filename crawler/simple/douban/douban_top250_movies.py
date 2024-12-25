"""
爬虫：豆瓣电影 TOP250 排行榜

@author: shiloh
@date: 2024/12/23 16:09
"""
import re

import requests
import xlsxwriter
from bs4 import BeautifulSoup

# 豆瓣电影TOP250排行榜页面地址
url = 'https://movie.douban.com/top250'
# 请求头
headers = {
    # 伪装成浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    # 模拟登录
    'Cookie': 'bid=47GW4LeeyQY; _pk_id.100001.4cf6=cfc8c9057f9277fc.1734940617.; ll="118286"; _vwo_uuid_v2=DFA415450A2114F634585374FAA05F078|ba8c7a99500b39f51ab9bff348b41c53; dbcl2="227337760:HLoGG6atpHE"; __utmz=30149280.1734943977.2.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1734943977.2.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; ck=XTyY; __utmc=30149280; __utmc=223695111; frodotk_db="c660b811a0336dbd53222834e09a4937"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1735107043%2C%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.889669202.1734940617.1735096661.1735107044.5; __utmb=30149280.0.10.1735107044; __utma=223695111.933700798.1734940617.1735096661.1735107044.5; __utmb=223695111.0.10.1735107044'
}
# 总电影数量
total_movies = 250
# 每页电影数量
page_size = 25


def get_movies() -> list[dict[str, object]]:
    """
    获取电影信息列表
    :return: 电影信息列表
    """

    movies = []
    for start in range(0, total_movies + 1, page_size):
        params = {
            'start': start
        }
        resp = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(resp.text, 'html.parser')
        movie_elements = soup.find('ol', class_='grid_view')
        for movie_item in movie_elements.find_all('div', class_='item'):
            movie = {}
            try:
                # 电影中文名称
                name_zh_tag = movie_item.find('span', class_='title')
                movie['name_zh'] = name_zh_tag.text.replace('\xa0', '')
                # 电影英文名称
                name_en_tag = name_zh_tag.find_next('span', class_='title')
                if name_en_tag:
                    movie['name_en'] = name_en_tag.text.replace('/', '').lstrip()

                # 封面图片地址
                movie['cover_src'] = movie_item.find('img')['src']
                # 电影详情链接
                movie['detail_url'] = movie_item.find('div', class_='hd').find('a')['href']
                # 评分信息
                star_div = movie_item.find('div', class_='star')
                # 评分分值
                movie['rating'] = star_div.find('span', class_='rating_num').text
                # 评价人数（去掉非数字内容）
                movie['total_raters']: str = re.sub(r'\D', "", list(star_div.children)[-2].text)
                # 概况
                movie['overview'] = movie_item.find('span', class_='inq').text

                bds = movie_item.find('div', class_='bd').find('p').text.replace('\n', '').split('...')
                infos = bds[1].replace('\xa0', '').strip().split('/')
                # 年份
                movie['year'] = infos[0]
                # 制片国家/地区
                movie['country'] = infos[1]
                # 类型
                movie['type'] = infos[2].replace(' ', '/')
                # 相关内容
                movie['bd'] = f'{bds[0].strip()}...'

                print(f'读取到一条电影信息：{movie}')
                movies.append(movie)
            except AttributeError as e:
                print(e)

            break

        # 休息 1 秒，避免被封IP
        # sleep(1.0)
        break

    return movies


# Excel 表头映射
excel_headers = {
    'name_zh': '电影中文名称',
    'name_en': '电影英文名称',
    'type': '类型',
    'year': '年份',
    'overview': '概况',
    'country': '制片国家/地区',
    'rating': '评分',
    'total_raters': '评价人数',
    'cover_src': '封面图片链接',
    'detail_url': '电影详情链接',
    'bd': '相关信息'
}


def export_to_excel(movies: list[dict[str, object]]):
    """
    导出电影信息列表到 Excel 文件中
    :param movies: 电影列表
    :return:
    """

    # 创建工作簿，并添加一个 sheet
    workbook = xlsxwriter.Workbook(r'D:\豆瓣电影Top250.xlsx')
    worksheet = workbook.add_worksheet('豆瓣电影Top250')

    # 指定标题行的单元格样式（加粗、居中、大小）
    cell_format = workbook.add_format(
        {'bold': True, 'align': 'center', 'valign': 'vcenter', 'font_size': '14'})
    worksheet.set_row(0, 30, cell_format)

    col = 0
    for key, value in excel_headers.items():
        worksheet.set_column(col, col, 25)
        worksheet.write(0, col, value)
        col += 1

    # 写入数据
    row = 1
    col = 0
    for movie in movies:
        print(f'写入一条电影信息：{movie}')
        for key in excel_headers.keys():
            worksheet.write(row, col, movie[key])
            col += 1

        col = 0
        row += 1

    workbook.close()


def main() -> None:
    """
    爬取豆瓣电影 Top250 排行榜数据
    """
    movies = get_movies()
    export_to_excel(movies)
    print("豆瓣电影 Top250 导出成功")


if __name__ == '__main__':
    main()
