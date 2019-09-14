# coding=utf-8

import wx


# 自定义窗口类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Box布局', size=(600, 300))
        self.Centre()  # 居中
        panel = wx.Panel(parent=self)
        # 创建垂直方向的Box布局对象
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel, label='快来尝试点击一下按钮吧！')
        # 添加静态文本到垂直Box管理器
        vbox.Add(self.statictext, proportion=2, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=10)

        b1 = wx.Button(parent=panel, id=10, label='按钮壹号')
        b2 = wx.Button(parent=panel, id=11, label='按钮贰号')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)
        # 创建水平方向的Box布局对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # 添加b1到水平Box布局管理
        hbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
        # 添加b2到水平Box布局管理
        hbox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)

        # 将水平Box布局管理器放到垂直BOX布局管理器
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)

        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('单击按钮壹号')
        else:
            self.statictext.SetLabelText('单击按钮贰号')


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('窗口关闭.....')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()

