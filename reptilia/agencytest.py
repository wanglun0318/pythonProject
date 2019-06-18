import urllib.request

url = "http://www.ip138.com/"
print(1111)
proxy_support = urllib.request.ProxyHandler({"HTTPS": "124.160.56.76:37511"})
print(1111)
opener = urllib.request.build_opener(proxy_support)
print(1111)
urllib.request.install_opener(opener)
print(1111)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"}
response = urllib.request.Request(url, headers)
req = urllib.request.urlopen(response).read()
html = req.read().decode("utf-8")
print(1111)
print(html)
