from tkinter import *

root = Tk()
root.geometry("200x200")

w1 = Button(root, text="多余空间靠左")
w1.pack(anchor="nw")

root.mainloop()