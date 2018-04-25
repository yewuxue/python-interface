#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
#用来操控部分请求过程，或信号事件处理
import requests
def print_url(r, *args, **kwargs):
    print(r.url)
requests.get('http://httpbin.org', hooks=dict(response=print_url))