# coding=utf-8

import wx


# 自定义窗口
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='StaticBox布局', size=(600, 300))
        self.Centre()  # 设置窗口居中
        panel = wx.Panel(parent=self)
        # 创建垂直方向管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel, label='你好!')
        # 添加静态文本到box布局管理器
        vbox.Add(self.statictext, proportion=2, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=10)

        b1 = wx.Button(parent=panel, id=10, label='确定')
        b2 = wx.Button(parent=panel, id=11, label='取消')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

        # 创建静态框对象
        sb = wx.StaticBox(panel, label='按钮框')
        # 创建水平方向的StaticBox管理器
        hsbox = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
        # 添加b1,b2到水平管理器中
        hsbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)

        # 添加hsbox到vbox
        vbox.Add(hsbox, proportion=1, flag=wx.CENTER)

        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('确定被点击了！')
        else:
            self.statictext.SetLabelText('取消被点击了！')

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('窗口已关闭....')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主程序循环

