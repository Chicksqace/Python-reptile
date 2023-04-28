#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/2 13:40
# @File :  Re库的基本使用.py
import re
# search
# match=re.search(r'[1-9]\d{5}','BIT 1008111111')
# if match:
#     print(match.group(0))
# match
# match=re.match(r'[1-9]\d{5}','1100081BIT 1008111111')
# if match:
#     print(match.group(0))
# findall
# match=re.findall(r'[1-9]\d{5}','1100081BIT 1008111111')
# if match:
#     print(match)
# split
# print(re.split(r'[1-9]\d{5}','BIT1004243 TsSU132323 9324348'))
# print(re.split(r'[1-9]\d{5}','BIT1004243 TsSU132323 9324348',maxsplit=1))
# findter
# for m in re.finditer(r'[1-9]\d{5}','BIT1004243 TsSU132323 9324348'):
#     if m:
#         print(m.group(0))

# sub
print(re.sub(r'[1-9]\d{5}','卧槽是','BIT1004243 TsSU132323 9324348'))