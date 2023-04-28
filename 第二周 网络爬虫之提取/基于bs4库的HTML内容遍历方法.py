#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/1 1:20
# @File : 基于bs4库的HTML内容遍历方法.py
from bs4 import BeautifulSoup
import requests
r=requests.get("https://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
# 向下遍历
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(len(soup.body.contents))
# 向上遍历
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
# 平行遍历
from bs4 import BeautifulSoup
import requests
r=requests.get("https://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
# print(soup.prettify())
print(soup.a.next_sibling)
for sibling in soup.a.next_siblings:
    print(sibling)
print("-----------")
print(soup.a.previous_sibling)
print(soup.a.previous_siblings)
for pre_sibling in soup.a.previous_siblings:
    print(pre_sibling)