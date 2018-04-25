#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests

#制订了一个单一的值作为 timeout,timeout 值将会用作 connect 和 read 二者的 timeout
r = requests.get('https://github.com', timeout=5)

#分别制定，就传入一个元组
r = requests.get('https://github.com', timeout=(3.05, 27))

#远端服务器很慢，你可以让 Request 永远等待，传入一个 None 作为 timeout 值
r = requests.get('https://github.com', timeout=None)