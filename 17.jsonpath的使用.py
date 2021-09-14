# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 16:14
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 17.jsonpath的使用.py
# @Software: PyCharm
import json
from jsonpath import jsonpath
import requests
from fake_useragent import UserAgent
'''
1.json模块的使用
'''
str = '{"user":"张三"}'
# 1.字符串类型转化成python中相应的类型
print(type(json.loads(str))) # <class 'dict'>
# 2.将python中的类型转化成字符串
print(type(json.dumps(str))) # <class 'str'>
print(json.dumps(str,ensure_ascii=False)) # "{\"user\":\"张三\"}"
# 3.将json的对象序列化到文件中
json.dump(json.loads(str),open('user.txt','w',encoding='utf-8'),ensure_ascii=False)
# 4.将文件中的json元素并转化成python类型
load = json.load(open('user.txt',encoding='utf-8')) # 不需要写打开的方式
print(load)

'''
2.jsonpath库的使用(解析json类型的数据)
'''
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

headers = {
    'User-Agent':UserAgent().chrome
}

response = requests.get(url, headers=headers)

names = jsonpath(response.json(), '$..name') # 获取城市名字
print(names)
print(jsonpath(json.loads(response.text),'$..allCitySearchLabels.A')[0][0])
