import tkinter as tk
from Bio.Seq import Seq

window = tk.Tk()

window.title("my window")
window.geometry("500x500")

e = tk.Entry(window, show=None,width=100)
e.pack(ipady=30)


def insert_point():
    var = e.get()
    var = Seq(var)  # 转为seq
    var = var.reverse_complement()
    t.insert("insert", var)


b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b1.pack()

t = tk.Text(window, height=8)
t.pack()

window.mainloop()
