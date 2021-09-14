# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 21:31
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : request对象的使用.py
# @Software: PyCharm
from urllib.request import urlopen
from urllib.request import Request
from random import choice
from fake_useragent import UserAgent
'''
    request对象用于封装请求头中的User-Agent信息
'''
url = 'https://www.baidu.com'

# 自定义定义User-Agent
user_agent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
              'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50']
# print(choice(user_agent))

# 定义请求头
# 使用fake_useragent库
agent = UserAgent()
headers = {
    # 'User-Agent':choice(user_agent) # 动态的生成User-Agent
    # 静态的定义User-Agent
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    'User-Agent':agent.chrome
}

request = Request(url,headers=headers)

# 发送请求
response = urlopen(request)

# 打印输入响应的内容
print(response.read().decode())
