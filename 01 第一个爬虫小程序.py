# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 21:17
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 01 第一个爬虫小程序.py
# @Software: PyCharm
from urllib.request import urlopen
# url
url = 'http://www.baidu.com'

# 发送请求
response = urlopen(url)

# 读取响应的内容
info = response.read()

# 打印输出响应的内容
print(info.decode())

# 打印输出响应的状态码
print(response.getcode())

# 打印输出真实的url
print(response.geturl())

# 打印输出响应头
print(response.info())
