# coding=utf-8
# 静态图片控件

import wx


# 创建窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态图片控件', size=(300, 300))
        # 创建图片对象
        self.bmps = [wx.Bitmap('images/bird5.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('images/bird4.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('images/bird3.gif', wx.BITMAP_TYPE_GIF)]
        self.Center()
        self.panel = wx.Panel(parent=self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        b1 = wx.Button(parent=self.panel, id=1, label='Button1')
        b2 = wx.Button(parent=self.panel, id=2, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)

        self.image = wx.StaticBitmap(self.panel, -1, self.bmps[0])  # self.bmps[0]默认显示

        # 添加标空件到BOX
        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(self.image, proportion=3, flag=wx.CENTER)

        self.panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 1:
            self.image.SetBitmap(self.bmps[1])
        else:
            self.image.SetBitmap(self.bmps[2])

        self.panel.Layout()  # 刷新panel


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('程序关闭...')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主程序循环
