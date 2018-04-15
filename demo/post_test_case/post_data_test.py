#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests
import json

host="http://httpbin.org/"
path="post"
url=''.join([host,path])
params={"show_env":1}
data={"a":"嘻嘻","b":"haha"}


'''给服务器发送请求'''
r=requests.post(url,params=params,data=data)
print(r.headers)
print(r.text)
