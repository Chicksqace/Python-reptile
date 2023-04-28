#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/31 23:16
# @File : Beautiful  Soup库的基本元素.py
import requests
from bs4 import BeautifulSoup
r=requests.get("https://python123.io/ws/demo.html")
# print(r.text)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
# tag
# print(soup.title)
# print(soup.a)
# print(soup.a.parent.name)

# atte
# print(soup.a.attrs)
# print(soup.a.attrs['class'])
# print(soup.a.attrs['href'])

# Tag的NavigableString
# print(soup.a.string)
# print(soup.p)
# print(soup.p.string)

# Tag的Comment
newsoup=BeautifulSoup("""
<b><!-- <h1>当前求和为：{{sum}}</h1> -->
<p>1234</p>
</b>
""","html.parser")
print(newsoup.b)
print(newsoup.b.p.string)
print(type(newsoup.b.p.string))
print(type(newsoup.b))