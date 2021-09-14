# -*- coding: utf-8 -*-
# @Time    : 2021/1/2 20:16
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 06 adjx请求的抓取.py
# @Software: PyCharm
'''
抓取豆瓣电影的信息（adjx请求）
'''
from urllib.request import urlopen,Request
from fake_useragent import UserAgent

base_url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20'

i = 0
while True:
    # 定义User-Agent
    headers = {
        'User-Agent':UserAgent().chrome
    }
    url = base_url.format(i * 20)
    # print(url)
    request = Request(url, headers=headers) # 对请求进行封装
    response = urlopen(request) # 发送请求，输出响应

    # 输出结果
    result_info = response.read().decode()
    i += 1
    if result_info == "" or result_info is None:
        print('已经没有数据啦...')
        break
    else:
        print(result_info)
