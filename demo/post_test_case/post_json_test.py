#！/usr/bin/python3
# -*- coding:UTF-8-*-
# author : YangShuang
import requests
import json

host="http://httpbin.org/"
path="post"
url=''.join([host,path])

data={
    "info":{"code":1,"sex":"男"},
    "code":1,
    "name":"嘻嘻"
}


'''给服务器发送请求'''
#r=requests.post(url,data=data)   这种方式无法传输内容
'''两种方式
r=requests.post(url,data=json.dumps(data))
r=requests.post(url,json=data)
'''
print(r.headers)
print(r.text)