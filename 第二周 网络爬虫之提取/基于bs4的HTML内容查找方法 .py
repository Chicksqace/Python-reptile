#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/1 14:27
# @File : 基于bs4的HTML内容查找方法 .py
from bs4 import BeautifulSoup
import requests
import re
r=requests.get("https://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
# name
# print(soup.find_all('a'))
# print(soup.find_all(['a','b']))
# attrs
# print(soup.find_all(id='link1'))
# print(soup.find_all(attrs={"class": "py1"}))
# print(soup.find_all(id=re.compile('link')))
#recursive 
# print(soup.find_all('a',recursive=True))
# print(soup.find_all('a',recursive=False))
# string
print(soup.find_all(string='Basic Python'))
# print(soup.find_all(string=re.compile('python')))
# 简写
print(soup(string='Basic Python'))