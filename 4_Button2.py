from tkinter import *

root = Tk()
root.geometry("200x200")


def addnum():
    num = int(b.cget("text"))  # 获取组件的参数选项
    b.config(text=str(num + 1))


b = Button(root, text="0", command=addnum,
           repeatdelay=1000, repeatinterval=500)
b.pack()

mainloop()