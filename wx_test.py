"""
学习wxpython的使用
"""

import wx


app=wx.App()
fram=wx.Frame(None,pos = (100,100), size=(800,600))
path_text= wx.TextCtrl(fram,pos=(5,5),size=(50,24))
button=wx.Button(fram,pos=(5,30),size=(50,24))
fram.Show()
app.MainLoop()
