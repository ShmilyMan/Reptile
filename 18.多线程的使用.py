# -*- coding: utf-8 -*-
# @Time    : 2021/1/8 17:14
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 18.多线程的使用.py
# @Software: PyCharm
from fake_useragent import UserAgent
import requests
from threading import Thread
from queue import Queue
import lxml.html

'''
使用多线程爬取糗事百科的段子数据
'''
# 爬虫类
class CrawlInfo(Thread):
    def __init__(self,url_queue,html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        headers = {
            'UserAgent':UserAgent().chrome
        }
        # 如果队列中还有值，则继续从队列中取
        while self.url_queue.empty() == False:
            response = requests.get(self.url_queue.get(), headers=headers)
            html_queue.put(response.text)

# 解析类
class SaveInfo(Thread):
    def __init__(self,html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        etree = lxml.html.etree
        while html_queue.empty() == False:
            etree_html = etree.HTML(html_queue.get())
            duanzi_info = etree_html.xpath("//div[@class='content']/span[1]")
            with open('newduanzi.txt','a',encoding='utf-8') as file: # 将结果写进文件
                for temp in duanzi_info:
                    info = temp.xpath('string(.)')
                    file.write(info)


if __name__ == '__main__':
    url_queue = Queue() # url的队列
    html_queue = Queue() # 保存响应信息的队列
    base_url = 'https://www.qiushibaike.com/text/page/{}/'
    for temp in range(1,14):
        url = base_url.format(temp)
        url_queue.put(url)

    # 开启三个线程
    for temp in range(0,3):
        crawl_info = CrawlInfo(url_queue,html_queue)
        crawl_info.run()

    # print(html_queue.qsize()) # html文档
    for temp in range(3):
        save_info = SaveInfo(html_queue)
        save_info.run()
