"""
获取反补基因序列
"""
import tkinter as tk
from tkinter import *
from Bio.Seq import Seq

root = Tk()
root.geometry("500x400")
root.iconbitmap("logo.ico")
root.title("获取反补基因序列")

lab_1 = Label(root, text="原始基因序列", font=("微软雅黑", 15), relief="sunken")
lab_1.place(x=50, y=20)

lab_2 = Label(root, text="反补基因序列", font=("微软雅黑", 15), relief="sunken")
lab_2.place(x=300, y=20)

text_1 = Text(root, width=15, height=12, font=("微软雅黑", 10))
text_1.place(x=50, y=70)

text_2 = Text(root, width=15, height=12, font=("微软雅黑", 10))
text_2.place(x=300, y=70)


def fan_bu():
    print(1)
    var = text_1.get("1.0", tk.END)
    var = Seq(var).reverse_complement()
    text_2.insert("end", var)


button_1 = Button(root, text="转换->", font=("微软雅黑", 15), command=fan_bu)
button_1.place(x=198, y=160)

mainloop()
