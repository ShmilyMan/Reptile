# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 18:09
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 14.Beautiful Soup的使用.py
# @Software: PyCharm
from bs4 import BeautifulSoup
from bs4.element import Comment
'''
使用BeautifulSoup解析[HTML文档（字符串的格式）]
'''
str = '''
<title class='a'>尚学堂</title>
<div class='info' float='left' id='user'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''

soup = BeautifulSoup(str, 'lxml') # 创建BeautifulSoup的对象
'''
一、只能获取检索到的第一个标签
'''
# 1.获取HTML文档的标签
print(soup.title) # 获取title标签 <title>尚学堂</title>
print(soup.div) # 获取div标签 <div class="info" float="left">Welcome to SXT</div> 只能获取第一个
# 2.获取HTML文档标签的属性
print(soup.div.get('class')) # ['info']
print(soup.div['class']) # ['info']
# 3.获取HTML文档标签的内容(两种方法)
print(soup.div.string) # Welcome to SXT
print(soup.div.text) # Welcome to SXT
# 4.获取HTML文档注释部分的内容以及非注释的内容（通过判断）
print(soup.strong.string) # 没用
print(soup.strong.text) # None
print(type(soup.strong.string))
if type(soup.strong.string) == Comment:
    print(soup.strong.string)
else:
    print(soup.strong.text)

'''
二、获取检索到的多个标签
'''
print('------------find_all()--------------')
# 通过id获取元素
print(soup.find_all(id='user')) # [<div class="info" float="left" id="user">Welcome to SXT</div>]
# 通过类属性获取元素
print(soup.find_all(_class='a')) # 不能使用
# 通过标签获取元素
print(soup.find_all('div'))
# 通过key:value获取元素,键值对的形式
print(soup.find_all(attrs={'float':'left'}))

print('----------------使用css样式表检索标签（select()）------------------')
# 通过id获取元素
print(soup.select('#user')) # [<div class="info" float="left" id="user">Welcome to SXT</div>]
# 通过类获取元素
print(soup.select('.info'))
'''
结果：
    [<div class="info" float="left" id="user">Welcome to SXT</div>, <div class="info" float="right">
    <span>Good Good Study</span>
    <a href="www.bjsxt.cn"></a>
    <strong><!--没用--></strong>
    </div>]
'''
# 通过标签获取元素
print(soup.select('title')) # [<title class="a">尚学堂</title>]
# 获取标签的子元素

print(type(soup.select('div')[1])) # <class 'bs4.element.Tag'> 列表中存放的是标签类型的对象

print(soup.select('div span')) # [<span>Good Good Study</span>]
print(soup.select('div > span')) # [<span>Good Good Study</span>]
print(soup.select('div')[1].select('a')[0].get('href')) # www.bjsxt.cn
