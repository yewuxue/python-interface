#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests
import json

host="http://httpbin.org/"
path="post"
url=''.join([host,path])

#1.普通上传
files={"files":open("testcases.txt","rb")}
#2.通过文件上传字符串
files1={"files":("testcases.txt","rbasasasa")}
#3.自定义文件名、文件类型以及请求头
files2={"files":("练习",open("testcases.jpg","rb"),"image/png")}
#4.传送多个文件
files3=[("files31",("练习",open("testcases.jpg","rb"))),
        ("files32",("练习1",open("testcases.jpg","rb")))
        ]
#5.流式上传
with open("testcase.txt") as f:
    r1 = requests.post(url, files=f)

r=requests.post(url,date=files)
print(r.text)