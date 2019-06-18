import urllib.request

# 下载一个猫图片
response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_ing = response.read()

with open("cat_200-300.jpg", "wb") as f:
    f.write(cat_ing)
