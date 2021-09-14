# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 22:00
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 11.requsts的使用.py
# @Software: PyCharm
import requests
from fake_useragent import UserAgent

'''
1.使用requests发送get请求
'''
url = 'https://www.qcc.com/gongsi_industry'

headers = {
    'User-Agent':UserAgent().chrome
}

params = {
    'industryCode':'C',
    'subIndustryCode':'14',
    'p':'2',
}

response = requests.get(url, params=params, headers=headers)

# 输出打印结果
print(response.text) # 使用字符串的形式，如果要使用字节的形式，则使用response.content

'''
2.使用request发送post请求
'''
# url = 'https://www.baidu.com/s'
#
# headers = {
#     'User-Agent':UserAgent().chrome
# }
#
# data = {
#     'user':'???',
#     'password':'???'
# }
#
# response = requests.get(url, data=data, headers=headers)

# 输出打印结果
# print(response.text) # 使用字符串的形式，如果要使用字节的形式，则使用response.content

'''
3.使用request使用代理发送请求
'''
# url = 'https://www.baidu.com/s'
# 
# headers = {
#     'User-Agent':UserAgent().chrome
# }
# 
# params = {
#     'wd':'尚学堂'
# }
# 
# proxies = {
#     'http':'118.252.9.242:8088'
# }
# 
# response = requests.get(url, params=params, headers=headers,proxies=proxies)
# 
# print(response.text)

'''
4.使用requests设置Session
'''
# # 登录
# session = requests.Session()
# url = 'https://www.baidu.com/s'
#
# headers = {
#     'User-Agent':UserAgent().chrome
# }
#
# data = {
#     'user':'???',
#     'password':'???'
# }
#
# response = session.get(url, data=data, headers=headers)
#
# # 访问登录后的页面
# url = ''
#
# headers = {
#     'User-Agent':UserAgent().chrome
# }
#
# response = session.get(url, data=data, headers=headers)
#
# #输出打印结果
# print(response.text) # 使用字符串的形式，如果要使用字节的形式，则使用response.content
'''
5.使用requests忽略网络安全证书
'''
# url = 'https://www.12306.cn/index/'
#
# headers = {
#     'User-Agent':UserAgent().chrome
# }
#
# # 忽略网页证书安全的警告
# requests.packages.urllib3.disable_warnings()
#
# response = requests.get(url, headers=headers, verify=False)
# response.encoding = 'utf-8' # 设置编码
# # 输出结果
# print(response.text)
