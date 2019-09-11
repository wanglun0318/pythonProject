# coding=utf-8

import wx


# 自定义窗口 类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='第一个GUI程序！', size=(400, 300))
        self.Center()  # 窗口居中
        panel = wx.Panel(parent=self)
        statictext = wx.StaticText(parent=panel, label='你好啊！', pos=(50, 50))


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('退出应用程序')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
