#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/29 21:44
# @File : Request库的get()方法.py
import requests
r=requests.get("http://www.baidu.com")
print(r.text)
print(r.apparent_encoding)
print(r.encoding)
r.encoding='utf-8'
print(r.text)
