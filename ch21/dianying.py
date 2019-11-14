# coding=utf-8


import bs4
import requests
import re

def geturl(url):
    res = requests.get(url)
    noStarchSoup = bs4.BeautifulSoup(res.text)
    return noStarchSoup

mainurl = geturl("http://gaoqing.la/")

for i in mainurl.select('a[class="zoom"]'):
    title = i.attrs['title']
    href = i.attrs['href']
    sonurl = geturl(href)
    a = 1

    for s in sonurl.select('a[style="color: #ff0000;"]'):
        magnet = s.attrs['href']
        # print(title, magnet)
        # print(s.attes('style'))
        type =re.findall(r'style="color: #ff0000;">(.*)', str(s))
        typeRight = re.sub(r'[</a>\'\[\]\s]', "", str(type))
        print("电影名称:{} 下载点{}:{} 下载连接:{} ".format(title, a, typeRight, magnet))
        a += 1
