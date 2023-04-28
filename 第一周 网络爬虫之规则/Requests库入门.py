#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/29 21:01
# @File : Requests库入门.py
import requests
r=requests.get("http://www.baidu.com")
print(r.text)