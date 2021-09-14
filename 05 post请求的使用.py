# -*- coding: utf-8 -*-
# @Time    : 2021/1/2 20:06
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 05 post请求的使用.py
# @Software: PyCharm

'''
post请求一般用于用户登录等操作
'''

from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

url = '...'

'''
定义data属性
'''
data = {
    'user':'xxx',
    'password':'123456'
}
data = urlencode(data)
'''
定义User-Agent
'''
headers = {
    'User-Agent':UserAgent().chrome
}
request = Request(url, data=data.encode(), headers=headers)
response = urlopen(request)

# 输出结果页面
print(response.read().decode())
