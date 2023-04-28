#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/9 15:47
# @File : test.py
def gen(n):
    for i in range(n):
        yield i**2
def gen1(n):
    for i in range(n):
        return i**2
for i in gen(5):
    print(i," ",end="")
for i in gen1(5):
    print(i," ",end="")