# coding=utf-8

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='一对一时间处理', size=(300, 180))
        self.Center()  # 窗口居中
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, pos=(110, 20))  # 创建静态文本
        b = wx.Button(parent=panel, label='OK', pos=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.on_click, b)   # 时间绑定

    def on_click(self, event):  # 点击按钮调用
        print(type(event))
        self.statictext.SetLabelText('hello, world.')


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('退出应用程序！')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
