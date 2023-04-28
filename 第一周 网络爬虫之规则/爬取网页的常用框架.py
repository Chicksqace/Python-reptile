#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/30 13:42
# @File : 爬取网页的常用框架.py
import requests

def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()#如果状态不是200，引发HTMLERROR异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__=="__main__":
    url="www.baidu.com"
    print(getHtmlText(url))