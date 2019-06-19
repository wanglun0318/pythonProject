import urllib.request
import random

# ip集合
ip_list = ["218.64.69.79:8080", "14.20.235.77:34100", "14.115.104.194:808"]

# 代理IP
url = "http://httpbin.org/get"

proxy_support = urllib.request.ProxyHandler({"http": random.choice(ip_list)})  # 随机使用一个IP
opener = urllib.request.build_opener(proxy_support)

# 添加 User-Agent
opener.addheaders = [{"User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"}]

urllib.request.install_opener(opener)
print(1111)
req = urllib.request.urlopen(url)
html = req.read().decode("utf-8")
print(html)
