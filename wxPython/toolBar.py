# coding=utf-8
# 使用工具栏

import wx
import wx.grid


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='使用工具栏', size=(550, 500))
        self.Center()
        self.Show(True)

        self.text = wx.TextCtrl(self, -1, style=wx.EXPAND | wx.TE_MULTILINE)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.text, proportion=1, flag=wx.EXPAND | wx.ALL, border=1)
        self.SetSizer(vbox)

        menubar = wx.MenuBar()                   # 创建菜单栏对象
        flie_menu = wx.Menu()                    # 创建文件菜单对象
        new_item = wx.MenuItem(flie_menu, wx.ID_NEW, text='新建', kind=wx.ITEM_NORMAL)   ## 创建新建菜单对象
        flie_menu.Append(new_item)               # 添加新建菜单项到文件菜单
        flie_menu.AppendSeparator()               # 添加分割线菜单

        edit_menu = wx.Menu()
        copy_item = wx.MenuItem(edit_menu, 100, text='复制', kind=wx.ITEM_NORMAL)
        edit_menu.Append(copy_item)

        cut_item = wx.MenuItem(edit_menu, 101, text='剪切', kind=wx.ITEM_NORMAL)
        edit_menu.Append(cut_item)

        paste_item = wx.MenuItem(edit_menu, 102, text='粘贴', kind=wx.ITEM_NORMAL)
        edit_menu.Append(paste_item)

        flie_menu.Append(wx.ID_ANY, '编辑', edit_menu)    # 添加编辑项到文件菜单

        menubar.Append(flie_menu, '文件')
        self.SetMenuBar(menubar)

        tb = wx.ToolBar(self, wx.ID_ANY)          # 创建工具栏对象
        self.ToolBar = tb        # 将工具栏赋值给顶级窗口的ToolBar属性，相当于在顶级创建中添加了工具栏
        tsize = (24, 24)
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, tsize)
        paste_bmp = wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR, tsize)

        tb.AddTool(10, 'New', new_bmp, kind=wx.ITEM_NORMAL, shortHelp='New')
        tb.AddTool(20, 'Open', open_bmp, kind=wx.ITEM_NORMAL, shortHelp='Open')
        tb.AddTool(30, 'Copy', copy_bmp, kind=wx.ITEM_NORMAL, shortHelp='Copy')
        tb.AddTool(40, 'Paste', paste_bmp, kind=wx.ITEM_NORMAL, shortHelp='Paste')
        tb.AddSeparator()

        tb.AddTool(201, 'back', wx.Bitmap('menu_icon/back.png'), kind=wx.ITEM_NORMAL, shortHelp='back')
        tb.AddTool(202, 'forward', wx.Bitmap('menu_icon/forward.png'), kind=wx.ITEM_NORMAL, shortHelp='forward')
        self.Bind(wx.EVT_MENU, self.on_click, id=201, id2=202)
        tb.AddSeparator()

        tb.Realize()          # 提交工具栏设置

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 201:
            self.text.SetLabel('单击【back】按钮')
        else:
            print('1111111111111111111')
            self.text.SetLabel('单击【forward】按钮')


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('程序关闭....')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主程序循环
