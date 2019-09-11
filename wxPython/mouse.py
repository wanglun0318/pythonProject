# coding=utf-8

import wx


# 自定义窗口类
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='鼠标事件处理', size=(400, 300))
        self.Center()
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)  # 绑定鼠标 按下事件
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)  # 绑定鼠标释放事件
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)  # 绑定鼠标按下移动事件

    def on_left_down(self, evt):
        print('鼠标按下......')

    def on_left_up(self, evt):
        print('鼠标释放.....')

    def on_mouse_move(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = event.GetPosition()
            print(pos)


class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('窗口关闭！')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
