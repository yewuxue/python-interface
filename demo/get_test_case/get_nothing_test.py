#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang

import requests
import json

host="http://httpbin.org/"
path="get"       #因为路径用的方法名，所以取名为path
url=''.join([host,path])


'''给服务器发送请求'''
r=requests.get(url)

# print(r.url)   #获取URL
print(r.status_code,r.reason) #获取状态码，获取状态码原因
# print(r.headers)#响应头
print(r.text)#unicode 文本信息
# print(r.content)#byte  图片或者文件
print(r.request.headers)#请求头
# print(r.request.method) #请求方法
# print(r.request.url)  #请求地址

'''把请求结果变成json串'''
response=r.json()    #返回的结果是字典模式