# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 23:18
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 15.xpath的使用.py
# @Software: PyCharm
import requests
from fake_useragent import UserAgent
import lxml.html

'''
爬取小说排行榜的数据
'''

url = 'http://www.biquge.info/paihangbang_allvisit/1.html'

headers = {
    'User-Agent':UserAgent().chrome
}

response = requests.get(url, headers=headers)
print(response.text)
# 创建etree对象
etree = lxml.html.etree
etree_html = etree.HTML(response.text)

names = etree_html.xpath("//span[@class='s2']/a/text()") # 获取小说的名字
types = etree_html.xpath("//span[@class='s1']/text()") # 获取小说的类型

# 第一种输出的方式
# for temp in range(len(names)):
#     print(types[temp] + ':' + names[temp])

# 第二种输出的方式,将两个参数进行压缩
for name,type in zip(names,types):
    # print(name + ':' + type)
    print(type,':',name)