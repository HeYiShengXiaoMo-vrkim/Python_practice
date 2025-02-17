from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Button的使用方法")
root.geometry("400x300")

def photo_1():
    messagebox.showinfo("提示", "你点击了第一个按钮")
    print("你点击了第一个按钮")

def photo_2():
    messagebox.showinfo("提示", "你点击了第二个按钮")
    print("你点击了第二个按钮")

photo = PhotoImage(file="D:\图片\DM_20240422154402_006.png")
Button(root, text="第一个按钮", command=photo_1, image=photo).pack()
Button(root, text="第二个按钮", command=photo_2).pack()
root.mainloop()