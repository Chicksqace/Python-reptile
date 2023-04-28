#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/30 14:55
# @File : 京东商品页面的爬取.py
import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
url="http://www.baidu.com/s"
keyword="Python"
try:
    kv={'wd':keyword}
    r=requests.get(url,headers=headers,params=kv)
    print(r.request.url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(len(r.text))
except:
    print('失败')
