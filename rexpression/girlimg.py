import urllib.request
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36")

    page = urllib.request.urlopen(req)
    html = page.read().decode("utf-8")
    print(2222)
    return html


def get_img(html):
    # 正则表达式
    #p = r'< img  class="BDE_Image" src="([^"]+\.jpg)">'
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    imglist = re.findall(p, html)
    print(11111)
    print(imglist)
    for each in imglist:

        print(each)


if __name__ == '__main__':
    # url = "https://tieba.baidu.com/p/6189168094"
    url = "http://cn-proxy.com"
    get_img(open_url(url))
    print(3333)
