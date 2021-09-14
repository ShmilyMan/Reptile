# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 20:32
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 07 https请求的使用.py
# @Software: PyCharm
from urllib.request import Request,urlopen
from fake_useragent import UserAgent
import ssl
'''
当https请求网页时出现证书认证错误，可以忽略网页的证书
'''
url = 'https://www.12306.cn/index/'
headers = {
    'User-Agent':UserAgent().chrome
}

request = Request(url, headers=headers)

# 忽略网页证书的认证
context = ssl._create_unverified_context()

response = urlopen(request,context=context)

# 输出结果
print(response.read().decode())
