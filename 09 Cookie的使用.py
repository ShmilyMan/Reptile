# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 21:23
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 09 Cookie的使用.py
# @Software: PyCharm
from urllib.request import urlopen,Request
from fake_useragent import UserAgent
'''
在访问有的网页时，有时候需要登录才能访问到网页
这是，在请求头中可以加入Cookie来携带用户Cookie来访问
也可以在登录时就记住Cookie并保存到本地文件中，再从本地文件中拿出Cookie进行访问需要访问的网页
'''
url = 'https://www.sxt.cn/profile/course'

headers = {
    'User-Agent':UserAgent().chrome,
    'Cookie':'UM_distinctid=176c2ecc4dc8f1-024fc11bd027e5-c791039-144000-176c2ecc4dd446; has_js=1; PHPSESSID=4aqhb8f820c55mrj2ci18p2686; 53revisit=1609588599881; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_land_page=https%253A%252F%252Fwww.sxt.cn%252Fjava%252Fjava-tutorial.html; kf_72085067_land_page_ok=1; CNZZDATA1261969808=1628332279-1609583878-https%253A%252F%252Fwww.baidu.com%252F%7C1609764748; 53kf_72085067_keyword=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dss1tOyuQIi_4FkK4_g6ZNq8_4s2HMsNTU4Q2C-_nE7vdluvxFa5g5lhSQox-lbKDGd-laEZ0MrI87pBK51_Qhq%26wd%3D%26eqid%3Dd09661fe00018c28000000035ff3173a; zg_did=%7B%22did%22%3A%20%22176c2f4e8e7516-0fef7c487b0bf3-c791039-144000-176c2f4e8e88b2%22%7D; zg_c1e08f0fa5e3446d854919ffa754d07f=%7B%22sid%22%3A%201609766725755%2C%22updated%22%3A%201609766807761%2C%22info%22%3A%201609588599039%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E8%AF%B8%E8%91%9Bio%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.sxt.cn%2Fjava%2Fjava-tutorial.html%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201609766725755%7D; user=a%3A2%3A%7Bs%3A2%3A%22id%22%3Bi%3A40283%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2215032317189%22%3B%7D'
}

request = Request(url, headers=headers)

response = urlopen(request)

# 输出响应的结果
print(response.read().decode())
