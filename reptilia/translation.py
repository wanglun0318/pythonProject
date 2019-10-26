import json
import urllib.request
import urllib.parse

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
data = {}
content = input("请输入需要翻译的内容：")
data["i"] = content
data["doctype"] = "json"
data["version"] = "2.1"
data["keyfrom"] = "fanyi.web"
data = urllib.parse.urlencode(data).encode("utf-8")
response = urllib.request.Request(url, data)
response.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400")
req = urllib.request.urlopen(response)
html = req.read().decode("utf-8")
print(html)
target = json.loads(html)
print(response.headers)
print(target)
print("翻译的结果是：{0}".format(target["translateResult"][0][0]["tgt"]))
{'type': 'ZH_CN2EN', 'errorCode': 0, 'elapsedTime': 1, 'translateResult': [[{'src': '爱', 'tgt': 'love'}]]}
