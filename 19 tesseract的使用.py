# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 20:15
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 19 tesseract的实验.py
# @Software: PyCharm
import pytesseract
from PIL import Image

'''
使用tesseract来识别图片的验证码
'''
# 1.打开文件
image = Image.open('yzm2.png')
# 2.识别图片验证码并返回一个字符串
image_string = pytesseract.image_to_string(image)
# 3.输出结果
print(image_string)
