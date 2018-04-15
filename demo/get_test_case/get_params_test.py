#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests
import json

host="http://httpbin.org/"
path="get"
url=''.join([host,path])
params={"show_env":1}

'''给服务器发送请求'''
r=requests.get(url,params=params)