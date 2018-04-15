#！/usr/bin/python3
# -*- coding:UTF-8-*-
# author : YangShuang
'''Cookiesz转换的两种方式
1.requests.utils.dict_from_cookiejar()将RequestsCookiesJar转换为字典
2.requests.utils.cookiejar_from_dict()将字典转换为RequestsCookiesJar
'''
import requests
import json

host="http://httpbin.org/"
path="cookies"       #因为路径用的方法名，所以取名为path
url=''.join([host,path])
url1="http://www.baidu.com"

'''给服务器发送请求'''
r=requests.get(url1)
print(r.cookies)   #获取cookies，没进行转换返回的来的是RequestsCookiesJar[]所以需要转换一下
c=requests.utils.dict_from_cookiejar(r.cookies)  #jar包转换为字典
print(c)
print({a.name:a.value for a in r.cookies}) #因为上面转换成的是伪字典，所以可以使用循环取出来

#发送Cookies到服务器
cookies={"cookies-name":"xixi"}
r1=requests.get(url,cookies=cookies)
print(r1.request.headers)
print(r1.text)

'''添加cookies的方法，需要保持session会话
1.s.cookies.set("cookie-name","cookie-value",path="/",domain=".abc.com")
2.requests.utils.add_dict_to_cookiejar(s.cookies,cookiedict)缺点：不能添加path和domain
'''
#复杂的写法
s=requests.session()
c=requests.cookies.RequestsCookieJar()
c.set("cookies-name","cookies-value",path="/",domain=".test.com")
s.cookies.update(c)
print(s.cookies)
