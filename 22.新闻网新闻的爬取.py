# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 17:47
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 22.新闻网新闻的爬取.py
# @Software: PyCharm
from fake_useragent import UserAgent
import requests
import lxml.html
'''
爬取电影的图片和文字
'''
url = 'https://movie.douban.com/subject/1292052/'
headers = {
    'User-Agent':UserAgent().chrome
}

response = requests.get(url, headers=headers)
# print(response.text)

etree = lxml.html.etree
etree_html = etree.HTML(response.text)
movie_head = etree_html.xpath('string(//h1)') # 电影的标题
movie_content = etree_html.xpath("string(//span[@class='all hidden'])") # 电影的描述
# print(movie_content)
img_url = etree_html.xpath("string(//div[@id='mainpic']/a/img/@src)") # 电影图片的地址

# 或取网页中的图片
url = img_url
movie_img = requests.get(url, headers=headers)
with open('.//movie.jpg','wb') as f:
    f.write(movie_img.content)
