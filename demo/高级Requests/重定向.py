#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests
r = requests.get('http://github.com')
r.url       #https://github.com/

#禁用重定向
r = requests.get('http://github.com', allow_redirects=False)

#使用了 HEAD，也可以启用重定向
r = requests.head('http://github.com', allow_redirects=True)
r.url