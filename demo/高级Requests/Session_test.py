#！/usr/bin/python3
# -*- coding:UTF-8-*-
# author : YangShuang
'''保持会话
session=requests.session()
session.get(url)
r=session.get(url)
'''
'''通过session保存一些会话信息
session.headers.update(headers1)
'''
'''删除已保存的会话信息，设置为none
session.headers["test1"]=None
'''

import requests
import json


host="http://httpbin.org/"
path="cookies/set/sessioncookie/123456"       #因为路径用的方法名，所以取名为path
url=''.join([host,path])
url1="http://httpbin.org/cookies"

'''给服务器发送请求'''
r=requests.get(url1)
'''保持会话'''
session=requests.session()    #初始化一个session对象
session.get(url) #cookies的信息存在session中
r1=session.get(url1)
print(r1.text)

'''通过session保存一些会话信息'''
header1={"test1":"aa"}
header2={"test2":"bb"}
session1=requests.session()
session1.headers.update(header1)   #已存在服务器中的信息
r2=session1.get("http://httpbin.org/headers",headers=header2)   #发送新的headers信息
print(r2.text)

'''删除已保存的会话信息，设置为none'''
session1.headers["test1"]=None  #删除已保存的会话信息
r3=session1.get("http://httpbin.org/headers",headers=header2)
print(r3.text)



