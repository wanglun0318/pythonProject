# coding=utf-8


import re
import json
import urllib.request


url = 'http://q.stock.sohu.com/hisHq?code=cn_600519&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp&0.8115656498417958'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode("gbk")
    print(htmlstr)
    htmlstr = htmlstr.replace('historySearchHandler([', '')  # 去掉 historySearchHandler([
    htmlstr = htmlstr.replace('])', '')                      # 去掉 ])
    print('替换后：', htmlstr)

    d = json.loads(htmlstr)
    print(d["hq"][0][1])

print("==========================================================")
for i in d["hq"]:
    print(i)
