#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import requests
#方法1 通过提供 proxies 参数来配置单个请求
proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
requests.get("http://example.org", proxies=proxies)

#方法2 环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理
'''
$export HTTP_PROXY="http://10.10.1.10:3128"
$ export HTTPS_PROXY="http://10.10.1.10:1080"
$ python
>>> import requests
>>> requests.get("http://example.org")
'''

#方法3 代理需要使用HTTP Basic Auth使用 http://user:password@host/ 语法
proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}

#方法4为某个特定的连接方式或者主机设置代理，使用 scheme://hostname 作为 key它会针对指定的主机和连接方式进行匹配。
proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}

#socks代理
#用 pip 获取依赖pip install requests[socks]
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}