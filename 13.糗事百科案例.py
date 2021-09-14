# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 12:55
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 13.糗事百科案例.py
# @Software: PyCharm
import requests
from fake_useragent import UserAgent
import re
'''
爬取糗事百科的段子
'''
base_url = 'https://www.qiushibaike.com/text/'
i = 0
while True:
    # https://www.qiushibaike.com/text/page/2/
    if i == 0:
        url = base_url
    else:
        url = 'https://www.qiushibaike.com/text/page/' + str(i) + '/'
    headers = {
        'User-Agent':UserAgent().chrome
    }
    print(url)
    response = requests.get(url, headers=headers)
    info = response.text
    i += 1
    # print(response.text)
    if i == 14:
        break  # 跳出循环
    if info != '' and info != None:
        # 进行正则匹配
        results = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>\s*</div>', info)

        # 将内容保存到文件中
        with open('duanzi.txt','a',encoding='utf-8') as file:
            for info in results:
                file.write(info + '\n')






