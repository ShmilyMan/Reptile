# -*- coding: utf-8 -*-
# @Time    : 2021/1/1 19:52
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 04 贴吧案例.py
# @Software: PyCharm
from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

'''
    获取贴吧的页面并保存获取的页面
    注意：endode()函数是编码函数，得到的结果是字节类型的
          decode()函数是解码函数，得到的结果是字符串类型的    
'''

'''
    发送请求，获取html信息
'''
def open_html(url):
    headers = {
        'User-Agent':UserAgent().chrome
    }
    request = Request(url,headers=headers)
    response = urlopen(request)
    # print(response.read().decode())
    # print(type(response.read().decode()))
    return response.read().decode() # 为字节信息

'''
    保存获取的html信息
'''
def save_html(bytes_html,fileName):
    with open(fileName,'w',encoding='utf-8') as file:
        file.write(bytes_html)

'''
    主方法
'''
def main():
    url = 'https://tieba.baidu.com/f?ie=utf-8&{}'
    # content = input('请输入要下载的内容：')
    # page_size = int(input('请输入要下载的页数：'))
    content = '尚学堂'
    page_size = 3
    for ps in range(page_size):
        args = {
            'kw': content,
            'pn': ps
        }
        fileName = '尚学堂第' + str(ps + 1) + '个页面.html'
        args = urlencode(args)
        str_htmlinfo = open_html(url.format(args))
        # print(str_htmlinfo)
        print('正在下载第' + str(ps + 1) + '页......')
        save_html(str_htmlinfo,fileName)

if __name__ == '__main__':
    main()