#！/usr/bin/python3
# -*- coding:UTF-8-*-
# author : YangShuang
import requests
host="http://httpbin.org/"
path="post"
url=''.join([host,path])
'''第一种普通形式上传文件
files={"files":open("test.txt","rb")}
r=requests.post(url,files=files)
'''
'''第二种形式字符串当作文件上传
files={"files":("qwer")}
r=requests.post(url,files=files)
'''
'''第三种自定义文件名、文件类型以及请求头。格式（请求文件名称、文件路径、文件类型、文件请求头）
#files={"files":open("qwe.jpg","rb")}   #最基本的   "files": "data:application/octet-stream;base64
files={"files":("嘻嘻哈哈.png",open("qwe.jpg","rb"),"image/png")}#更改以后   "files": "data:image/png;base64
r=requests.post(url,files=files)
'''
'''第四种 传送多个文件
# files=[
#     ("field1",("test.txt",open("test.txt","rb"))),
#     ("field2",("qwe.jpg",open("qwe.jpg","rb")))
# ]
files=[
    ("field1",open("test.txt","rb")),
    ("field2",open("qwe.jpg","rb"))
]
r=requests.post(url,files=files)
'''
'''第五种 流式上传
with open("test.txt") as  files:
    r = requests.post(url, data=files)
'''
