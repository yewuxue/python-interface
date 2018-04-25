#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests
import json

host="http://httpbin.org/"
path="post"
url=''.join([host,path])
params={"show_env":1}
data={
    "info":{"a":"嘻嘻","b":"haha"},
    "code":1,
    "id":9000
}


'''给服务器发送请求'''
#r=requests.post(url,params=params,data=json.dumps(data))
r1=requests.post(url,params=params,json=data)
res=r1.json()
#print(r1.headers)
print(res["json"])
