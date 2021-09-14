# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 18:11
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 23.将数据保存到Excel表中.py
# @Software: PyCharm

'''
往Excel表中添加数据
'''

import xlwt

workbook = xlwt.Workbook(encoding='utf-8')       # 创建一个Excel对象
sheet = workbook.add_sheet('sheet1')             # 在Excel中创建第一个表
# sheet.write(0, 0, 'hello')                      # 写入数据
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            sheet.write(i-1,j-1,f'{i}*{j}={i*j}')
workbook.save('1.xls')                           # 将数据保存到硬盘中




