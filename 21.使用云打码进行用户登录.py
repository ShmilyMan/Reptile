# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 13:29
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 21.使用云打码进行用户登录.py
# @Software: PyCharm
from fake_useragent import UserAgent
import requests
import base64
import json
import requests

# 发送请求，识别验证码
def base64_api(uname, pwd,  img):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

# 下载图片以及获取图片的验证码
def get_code():
    url_image = 'http://web.dowei.net/public/safecode.asp'
    code_image = session.get(url_image, headers=headers)
    with open('code.png','wb') as f:
        f.write(code_image.content)
    img_path = "code.png"
    result = base64_api(uname='wxl', pwd='wxl195920', img=img_path)

# 登录
def login():
    login_url = 'http://web.900112.com/action/CheckLogin.asp'
    params = {
        'loginname':'wxlaaa',
        'loginpwd':'wxl195920',
        'VerifyCode':code
    }
    login_html = requests.post(login_url, headers=headers, params=params)
    print(login_html.text)

if __name__ == '__main__':
    url = 'http://web.900112.com/login.html'
    headers = {
        'User-Agent':UserAgent().chrome
    }
    session = requests.Session()
    response = session.get(url, headers=headers)
    code = get_code() # 获取验证码
    print(code)
    login() # 登录
