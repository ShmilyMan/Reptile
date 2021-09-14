# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 20:39
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 08 proxy的使用.py
# @Software: PyCharm
from urllib.request import Request,urlopen
from urllib.request import build_opener
from urllib.request import ProxyHandler
from fake_useragent import UserAgent
'''
使用代理的ip来爬取网页，防止自己的ip被封
'''
url = 'http://httpbin.org/get'

headers = {
    'User-Agent':UserAgent().chrome
}

request = Request(url,headers=headers)

# 使用代理来请求服务器
'''
形式：
    1.免费的：
        '请求的协议':'IP:port'
    2.购买的：
        '请求的协议':'username:password@IP:port'
'''
proxy_handler = ProxyHandler({'http':'http://118.252.9.242:8088'})
opener = build_opener(proxy_handler)
response = opener.open(request)  # urlopener()封装好的

# 输出请求的结果
print(response.read().decode())
