#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/30 14:11
# @File : HTTP协议及Request库方法.py
import requests
r=requests.head('http://baidu.com')
print(r.headers)
print(r.text)