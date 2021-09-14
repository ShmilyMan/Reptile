# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 0:13
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 16.pyquery的使用.py
# @Software: PyCharm
import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq

url = 'https://www.kuaidaili.com/free/' # 请求的网址t

# 定义请求头
headers = {
    'User-Agent':UserAgent().chrome
}

response = requests.get(url, headers=headers) # 发送请求

# print(response.text)
doc = pq(response.text)

'''
先获取每个tr，再分别循环遍历输出要输出的内容
'''
trs = types = doc('tbody tr') # 获取所有的表单项
for temp in range(len(trs)):
    type = trs.eq(temp).find('td').eq(3).text()
    ip = trs.eq(temp).find('td').eq(0).text()
    port = trs.eq(temp).find('td').eq(1).text()
    print('端口号：',port,'IP：',ip,'类型：',type)