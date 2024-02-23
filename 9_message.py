import tkinter as tk
from tkinter import *
from Bio.Seq import Seq
root = Tk()
root.geometry("400x500")
root.iconbitmap("logo.ico")
root.title("插入图片")


# root.config(bg="blue")

def button_click():
    print("点了一下按钮！！！")


image = PhotoImage(file="五角星.gif")
lb = Label(root, image=image, text="五角星", font=("微软雅黑", 18), compound="top")
lb.place(x=50, y=20)
# lb.pack()

lab = Label(root, text="Hello, Tkinter!", relief="sunken")
lab.place(x=200, y=20)

var = tk.StringVar()
var.set("16")
sth = var.get()
print(sth)

button1 = Button(root, text="按钮1", font=("微软雅黑", 18), command=button_click, width=10, height=1)
button1.place(x=200, y=100)

fr = LabelFrame(root, text="LabelFrame")
fr.place(x=50, y=180)

Button(fr, text="1", font=("微软雅黑", 18)).pack()
Button(fr, text="2", font=("微软雅黑", 18)).pack()

ent1 = Entry(root, show="*", font=("微软雅黑", 15))
ent1.place(x=150, y=200)

ent2 = Entry(root, show="", font=("微软雅黑", 15))
ent2.place(x=150, y=250)


def print_get():
    print(ent3.get())


ent3 = Entry(root, show="", font=("微软雅黑", 15))
ent3.place(x=150, y=300)

button2 = Button(root, text="获取输入", command=print_get)
button2.place(x=50, y=320)

tx1 = Text(root, width=10, height=5)
tx1.place(x=150, y=350)

tx2 = Text(root, width=10, height=5)
tx2.place(x=250, y=350)


def zuan_hua():
    var_y = tx1.get("1.0", tk.END)
    var_y = Seq(var_y).reverse_complement()
    tx2.insert(END, var_y)
    print(var_y)


button3 = Button(root, text="转化", command=zuan_hua)
button3.place(x=350, y=350)

var1 = tk.StringVar()
var1.set("苍茫的天涯是我的爱，绵绵的青山脚下花盛开。")

message = Message(root, bg="light yellow", textvariable=var1, font="times 12 italic")
message.place(x=20, y=350)

mainloop()
