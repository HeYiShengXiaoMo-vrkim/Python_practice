from tkinter import *

import messagebox

root = Tk()
root.title("Radiobutton")
root.geometry("500x500")

# 初始化变量的值
v = StringVar()
v.set("M")

r1 = Radiobutton(root, text="男", variable=v, value="M")
r1.pack()
r2 = Radiobutton(root, text="女", variable=v, value="F")
r2.pack()
def confirm():
    print("用户选择的性别：", v.get())  # get获得的是value
    messagebox.showinfo("提示", "用户选择的性别：{}".format(v.get()))
Button(root, text="确定", command=confirm).pack()
root.mainloop()