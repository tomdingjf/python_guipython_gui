from tkinter import *

root = Tk()
root.geometry("400x200")

Button(root, text="0行0列").grid(row=0, column=0)
Button(root, text="1行0列").grid(row=1, column=0)
Button(root, text="0行1列(占两行)").grid(row=0, column=1, rowspan=2)

root.mainloop()