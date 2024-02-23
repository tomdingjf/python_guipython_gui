#建立一个tkinter变量的方法是：
# var = tkinter.StringVar()
# 然后就可以设置变量的值：
# var.set(value)
# 也可以获取变量的值：
# sth = var.get()
from tkinter import *

root = Tk()


def callback():
    print("你点了一下按钮")


button = Button(root, text="按钮", command=callback)
Button(root, text="按钮", activeforeground="blue", activebackground="yellow")
button.pack()

mainloop()