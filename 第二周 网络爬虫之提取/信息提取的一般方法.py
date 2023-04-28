#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/1 13:31
# @File : 信息提取的一般方法.py
from bs4 import BeautifulSoup
import requests
r=requests.get("https://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
for link in soup.find_all("a"):
    print(link.get("href"))