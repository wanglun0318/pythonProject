class Rectangle:
    length = 5
    width = 4

    def setRect(self):
        print("请输入矩形的长和宽....")
        self.length = format(input("长："))
        self.width = format(input("宽："))

    def getRect(self):
        print("这个矩形的长是：{0}，宽是：{1}".format(self.length, self.width))

    def getAres(self):
        return int(self.length) * int(self.width)


a = Rectangle()
a.setRect()
a.getRect()
print("这个长方形的面积是：{0}".format(a.getAres()))
