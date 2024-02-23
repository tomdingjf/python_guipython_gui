"""
引用tkinter.colorchooser包
颜色选择对话框
 askcolor()函数弹出模式颜色选择对话框
 返回形式为包含RGB十进制浮点元组和RGB十六进制字符串的元组类型
"""
from tkinter import *
import tkinter.colorchooser


def xz():
    color = tkinter.colorchooser.askcolor()
    colorstr = str(color)
    print('打印字符串%s 切掉后=%s' % (colorstr, colorstr[-9:-2]))
    lb.config(text=colorstr[-9:-2], background=colorstr[-9:-2])


root = Tk()

lb = Label(root, text='请关注颜色的变化')
lb.pack()
btn = Button(root, text='弹出颜色选择对话框', command=xz)
btn.pack()
root.mainloop()
