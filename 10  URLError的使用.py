# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 21:37
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 10  URLError的使用.py
# @Software: PyCharm
from urllib.request import urlopen,Request
from fake_useragent import UserAgent
from urllib.error import URLError
'''
可以使用URLError类来抓取各种类型的异常，并根据异常来判断程序错误的类型
'''
url = 'https://www.sxtq.cn/'

headers = {
    'User-Agent':UserAgent().chrome
}

try:
    request = Request(url, headers=headers)
    response = urlopen(request)
    print(response.read().decode())
except URLError as e:
    if e.args == ():
        print(e.code)
    else:
        print(e.args[0].errno)

print('下载完成...')
