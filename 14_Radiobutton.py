from tkinter import *
"""
单选按钮
"""

def mysel():
    dic = {0: "甲", 1: "乙", 2: "丙"}
    s = "您选择了" + dic.get(var.get()) + "项"
    lb.config(text=s)


root = Tk()
root.title("单选按钮")
lb = Label(root)
lb.pack()

var = IntVar()
rd1 = Radiobutton(root, text="甲", variable=var, value=0, command=mysel)
rd1.pack()

rd2 = Radiobutton(root, text="乙", variable=var, value=1, command=mysel)
rd2.pack()

rd3 = Radiobutton(root, text="丙", variable=var, value=2, command=mysel)
rd3.pack()

root.mainloop()
