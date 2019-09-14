# coding=utf-8

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='FlexGrid布局', size=(400, 200))
        self.Center()  # 窗口居中
        panel = wx.Panel(parent=self)

        # 创建一个3行2列，水平跟垂直间隙为10的FlexGridSizer对象
        fgs = wx.FlexGridSizer(3, 2, 10, 10)

        title = wx.StaticText(panel, label='标题：')
        author = wx.StaticText(panel, label='作者名：')
        review = wx.StaticText(panel, label='内容：')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        # 添加控件到FlexGridSizer
        fgs.AddMany([
            title, (tc1, 1, wx.EXPAND),
            author, (tc2, 1, wx.EXPAND),
            review, (tc3, 1, wx.EXPAND)
        ])

        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 2)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        panel.SetSizer(hbox)


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
    app.MainLoop()  # 进入主事件循环
