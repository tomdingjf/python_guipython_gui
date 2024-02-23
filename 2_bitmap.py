from tkinter import *


# bitmap参数
# bitmap参数指定添加位图，即内置图标，有error, info, hourglass, questhead, question, warning, gray12, gray25, gray50, gray75。
root = Tk()

bitmaps = ["error", "info", "hourglass", "questhead", "question", "warning",
           "gray12", "gray25", "gray50", "gray75"]
for bitmap in bitmaps:
    Label(root, text=bitmap, bitmap=bitmap, compound="left").pack()

mainloop()