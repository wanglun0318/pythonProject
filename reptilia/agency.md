# 代理

- 步骤：
    - 1.参数是一个字典{"类型":"代理IP:端口号"}
        - proxy_support = urllib.request.ProxyHandler({})
    - 2.定制，创建一个opener
        - opener = urllib.request.build_opener(proxy_support)
    - 3.a.安装opener
        - urllib.request.install_opener(opener)
    - 3.b.调用opener
        - opener.open(url)
