# coding=utf-8
# 静态文本和按钮

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态文本和按钮', size=(300, 200))
        self.Center()  # 窗口居中
        panel = wx.Panel(parent=self)
        # 创建垂直方向的BOX布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.statictext = wx.StaticText(parent=panel, label='StaticText1', style=wx.ALIGN_CENTER_HORIZONTAL)
        b1 = wx.Button(parent=panel, label='OK', id=1)
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1)

        b2 = wx.ToggleButton(panel, id=2, label='ToggleButton')
        self.Bind(wx.EVT_TOGGLEBUTTON, self.on_click, id=2)

        bmp = wx.Bitmap('icon/1.png', wx.BITMAP_TYPE_PNG)
        b3 = wx.BitmapButton(panel, 3, bmp)
        self.Bind(wx.EVT_BUTTON, self.on_click, id=3)

        # 添加静态文本和按钮到BOX
        vbox.Add(100, 10, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b3, proportion=1, flag=wx.CENTER | wx.EXPAND)

        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 1:
            self.statictext.SetLabelText('Button被点击！')
        if event_id == 3:
            self.statictext.SetLabelText('BitmapButton被点击！')
        if event_id == 2:
            self.statictext.SetLabelText('ToggleButton被点击！')


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('窗口关闭...')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主时间循环
