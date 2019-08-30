import re

# print(re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-4])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-4])", "192.168.25.111"))

print(re.search(r'<img class="BDE_Image" src="([^"]+\.jpg)', '<img class="BDE_Image" src="https://imgsa.baidu.com/sign=fcf0ba6344ed2e73fce98624b700a16d/c5f835fa828ba61e62599dc84f34970a324e59eb.jpg'))

# <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=fcf0ba6344ed2e73fce98624b700a16d/c5f835fa828ba61e62599dc84f34970a324e59eb.jpg">

