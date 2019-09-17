# coding=utf-8
# 文本输入控件

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态文本和按钮', size=(400, 200))
        self.Center()  # 窗口居中
        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(3, 2, 10, 10)  # 网格控件

        uesrid = wx.StaticText(panel, label='用户ID：')
        pwd = wx.StaticText(panel, label='密码：')
        content = wx.StaticText(panel, label='多行文本：')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        # 设置tcl初始值
        tc1.SetValue('tony')
        # 获取tc1值
        print('读取用户ID：{0}'.format(tc1.GetValue()))

        fgs.AddMany([uesrid, (tc1, 1, wx.EXPAND),
                     pwd, (tc2, 1, wx.EXPAND),
                     content, (tc3, 1, wx.EXPAND)])
        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 2)
        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)


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
