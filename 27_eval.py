import tkinter as tk


def button_click(value):
    """
    获取按键点击的数值
    :param value:
    :return:
    """
    current = entry.get()  # 获取当时输入框的值
    entry.delete(0, tk.END)  # 从开头到结尾，删除，即：清空输入框
    entry.insert(tk.END, current + value)  # 将输入的值赋值到输入框中


def clear():
    """
    清空
    :return: None
    """
    entry.delete(0, tk.END)  # 从开头到结尾，删除，即：清空输入框


def calculate():
    """
    计算简单算数
    :return: 返回计算结果
    """
    try:  # 如果正确则运行以下代码
        result = eval(entry.get())  # eval 可计算字符串
        entry.delete(0, tk.END)  # 清空输入框
        entry.insert(tk.END, str(result))  # 将结果赋值到输入框中
    except:  # 如果有无则运行以下代码
        entry.delete(0, tk.END)  # 清空输入框
        entry.insert(tk.END, "Error")  # 将Error赋值到输入框中


root = tk.Tk()  # 定义主窗口，即主Frame
root.title("简单计算器")  # 定义标题

entry = tk.Entry(root, width=35, borderwidth=5, font=("微软雅黑", 15))  # 设置输入框大小
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # 设置输入框显示位置

# 设置按钮的显示文本和位置到列表，里面套着元组
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    if text != "C" and text != "=":
        # 当选中数字时运行以下代码
        # 匿名函数 lambda 传入参数 : 函数体
        # 此处不用名称函数是因为 command= 后面只能是函数名，不能进行传参
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda value=text: button_click(value))
        button.grid(row=row, column=col)
    elif text == "C":
        # 当选择清除时运行以下代码
        button = tk.Button(root, text=text, padx=40, pady=20, command=clear)
        button.grid(row=row, column=col)
    else:
        # 当选择=时运行以下代码进行计算
        button = tk.Button(root, text=text, padx=40, pady=20, command=calculate)
        button.grid(row=row, column=col)

root.mainloop()
