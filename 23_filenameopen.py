"""
文件选择对话框
可弹出文件选择对话框，让用户直观地选择一个或一组文件，以供进一步的文件操作。
askopenfilename()、askopenfilenames()和asksaveasfilename(),
用于进一步打开一个文件、一组文件和保存文件。
askopenfilename()和asksaveasfilenamme()函数的返回值类型为包含文件路径的文件名字符串，而askopenfilenames()函数的返回值类型为元组。
"""
from tkinter import *
import tkinter.filedialog


def xz():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        lb.config(text='您选择的文件是' + filename)
    else:
        lb.config(text='您没有选择任何文件')


root = Tk()

lb = Label(root, text='')
lb.pack()
btn = Button(root, text='弹出文件选择对话框', command=xz)
btn.pack()
root.mainloop()
