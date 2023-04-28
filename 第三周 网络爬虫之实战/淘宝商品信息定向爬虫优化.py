import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'"view_price":"([\d\.]*)"', html)
        tlt = re.findall(r'"raw_title":"(.*?)"', html)
        for price, title in zip(plt, tlt):
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    print(f'{"序号":4}\t{"价格":8}\t{"商品名称":16}')
    count = 0
    for g in ilt:
        count += 1
        print(f'{count:4}\t{g[0]:8}\t{g[1]:16}')


def main():
    goods = '书包'
    depth = 3
    start_url = f'https://s.taobao.com/search?q={goods}'
    infoList = []
    for i in range(depth):
        try:
            url = f'{start_url}&s={44*i}'
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


if __name__ == '__main__':
    main()