# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 11:55
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 12.re正则表达式的使用.py
# @Software: PyCharm
import re

str = 'I Study Python3.7 Everyday'
# 从头开始匹配
print('-----------match()--------------')
# 匹配字符I
m1 = re.match(r'I',str)
m2 = re.match(r'\w',str) # 匹配字母数字下划线
m3 = re.match(r'\S',str) # 匹配非空白的字符
m4 = re.match(r'\D',str) # 匹配非数字的字符
m5 = re.match(r'i',str,re.I) # re.I大小写不敏感
m6 = re.match(r'.',str) # 匹配任意一个字符
# m7 = re.match(r'Study',str) # 匹配不上，因为match()是从头也就是从第一个字母开始匹配
print(m6.group())


# 匹配全部的字符串，不是从头开始匹配
print('-----------search()--------------')
# 匹配Study
s1 = re.search(r'Study',str)
s2 = re.search(r'S\w+',str)
print(s2.group())
# 匹配Python3.7
s3 = re.search(r'P\w+.\d',str) # .可以匹配任意一个字符
print(s3.group())


# 查找所有的匹配的结果
print('-----------findall()--------------')
f1 = re.findall(r'y',str)
print(f1) # ['y', 'y', 'y', 'y']


'''
练习
'''
str2 = '<div><a herf = "http://www.bjsxt.com">bjsxt尚学堂</a></div>'
print('-----------test()--------------')
# 匹配a标签里面的内容
result1 = re.findall(r'<a herf = "http://www.bjsxt.com">(.+)</a>', str2)
print(result1)

# 匹配herf链接的网址
result2 = re.findall(r'<a herf = "(.+)">bjsxt尚学堂</a>',str2)
print(result2)

# 将div标签替换成span标签
result3 = re.sub(r'<div>(.+)</div>',r'<span>\1</span>',str2)
print(result3)