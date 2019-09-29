# coding=utf-8
# 使用菜单

import wx
import wx.grid


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='使用菜单', size=(550, 500))
        self.Center()  # 窗口居中

        self.text = wx.TextCtrl(self, -1, style=wx.EXPAND | wx.TE_MULTILINE)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.text, proportion=1, flag=wx.EXPAND | wx.ALL, border=1)
        self.SetSizer(vbox)

        menubar = wx.MenuBar()              # 创建菜单栏对象
        file_menu = wx.Menu()              # 创建‘文件’菜单对象
        new_item = wx.MenuItem(file_menu, wx.ID_NEW, text='新建', kind=wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.on_newitem_click, id=wx.ID_NEW)
        file_menu.Append(new_item)
        file_menu.AppendSeparator()        # 添加分割线菜单项

        edit_menu = wx.Menu()
        copy_item = wx.MenuItem(edit_menu, 100, text='复制', kind=wx.ITEM_NORMAL)
        edit_menu.Append(copy_item)

        cut_item = wx.MenuItem(edit_menu, 101, text='剪切', kind=wx.ITEM_NORMAL)
        edit_menu.Append(cut_item)

        paste_item = wx.MenuItem(edit_menu, 102, text='黏贴', kind=wx.ITEM_NORMAL)
        edit_menu.Append(paste_item)
        self.Bind(wx.EVT_MENU, self.on_editmenu_click, id=100, id2=102)
        file_menu.Append(wx.ID_ANY, "编辑", edit_menu)

        menubar.Append(file_menu, '文件')
        self.SetMenuBar(menubar)

    def on_newitem_click(self, event):
        print('111111')
        self.text.SetLabel('单击【新建】菜单')

    def on_editmenu_click(self, event):
        event_id = event.GetId()
        if event_id == 100:
            self.text.SetLabel('单击【复制】菜单')
        elif event_id == 101:
            self.text.SetLabel('单击【剪切】菜单')
        else:
            self.text.SetLabel('单击【粘贴】菜单')


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('程序关闭......')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()   # 进入主程序循环



