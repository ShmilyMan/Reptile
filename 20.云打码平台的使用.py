# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 11:48
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 20.云打码平台的使用.py
# @Software: PyCharm
import base64
import json
import requests

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


if __name__ == "__main__":
    img_path = "yzm1.png"
    result = base64_api(uname='wxl', pwd='wxl195920', img=img_path)
    print(result)