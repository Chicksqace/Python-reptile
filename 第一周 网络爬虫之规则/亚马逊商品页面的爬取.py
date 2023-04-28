#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/3/30 14:55
# @File : 京东商品页面的爬取.py
import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    r=requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print('失败')
print(r.status_code)
print(r.apparent_encoding)
print(r.text[:10000])