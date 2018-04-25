#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests

#基础认证一般是64位加密,方法1
r=requests.get("http://httpbin.org/basic-auth/user/passwd",auth=("user","passwd"))
print(r.text)

#方法2
from requests.auth import HTTPBasicAuth
r1=requests.get("http://httpbin.org/basic-auth/user/passwd",auth=HTTPBasicAuth("user","passwd"))
print(r1.text)

#Digest一般是MD5加密
from requests.auth import HTTPDigestAuth
r2=requests.get("http://httpbin.org/digest-auth/auth/user/passwd/MD5",auth=HTTPDigestAuth("user","passwd"))
print(r2.text)

#Oauth授权
headers={"Authorization":"token wqeryuiweqry324234234"}
response=requests.get("url",headers=headers)

#证书认证 SSL认证
requests.get("url",verify=True)
requests.get('https://github.com', verify='/path/to/certfile') #也可以传入ca证书文件夹路径

#客户端认证
requests.get("url",cert=("/path/serer.crt","/path/key"))

#自定义身份认证
#自定义的身份认证机制是作为requests.auth.AuthBase的子类来实现的
from requests.auth import AuthBase
class PizzaAuth(AuthBase):
    def __init__(self, username):
        self.username = username
    def __call__(self, r):
        r.headers['X-Pizza'] = self.username
        return r
requests.get("url",auth=PizzaAuth("kenenth"))