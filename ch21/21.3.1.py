# coding=utf-8

import urllib.request
import os
import re

url = 'http://p.weather.com.cn/'

def findallimgurl(htmlstr):
    # 从HTML代码中查找匹配的字符串
    pattern = r'http://\S+(?:\.png|\.jpg)'
    return re.findall(pattern, htmlstr)


def getfilename(urlstr):
    # 根据图片连接地址截取图片名
    pos = urlstr.rfind('/')     # 对字符串进行从右向左查找
    print(pos)                  # 然后进行分片操作
    return urlstr[pos + 1:]


# 分析获得的url列表
url_list = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    url_list = findallimgurl(htmlstr)
    print(url_list)

for imagesrc in url_list:
    req = urllib.request.Request(imagesrc)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        # 过滤小于10kb的图片
        if len(data) < 1024 * 100:
            continue

        # 创建download文件夹
        if not os.path.exists('download'):
            os.mkdir('download')

        # 获取文件名
        filename = getfilename(imagesrc)
        filename = 'download/' + filename
        # 保存图片
        with open(filename, 'wb') as f:
            f.write(data)
    print('下载图片', filename)
