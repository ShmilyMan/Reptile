# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 11:39
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 03 get请求的使用.py
# @Software: PyCharm
from urllib.request import urlopen,Request
from urllib.parse import urlencode
from urllib.parse import quote
from fake_useragent import UserAgent

# 使用urlencode进行转码,可以转多个键值对
args = {
    'wd':'尚学堂'
}

# print(urlencode(args))
# url = f'https://www.baidu.com/s?{urlencode(args)}'

# 使用quote进行转码
# print(quote('尚学堂'))
url = 'https://www.baidu.com/s?wd={}'.format(quote('尚学堂'))
# 定义请求头
headers = {
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    'User-Agent':UserAgent().random # 使用随机的User-Agent
}

request = Request(url,headers=headers)

# 发送请求
response = urlopen(request)

# 输出响应的文本内容
print(response.read().decode())
