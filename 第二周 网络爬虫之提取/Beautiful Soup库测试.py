#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/30 22:52
# @File : Beautiful Soup库测试.py
import requests
from bs4 import BeautifulSoup
r=requests.get("https://python123.io/ws/demo.html")
# print(r.text)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.prettify())
