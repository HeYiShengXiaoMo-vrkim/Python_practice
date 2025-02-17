from tkinter import *

def confirm():
    print("用户名：", v1.get())
    print("密码：", v2.get())

root = Tk()
root.title("登录界面")
root.geometry("300x200+500+300")# 窗口大小和位置
label1 = Label(root, text="用户名：")
label1.pack()
v1 = StringVar()
entry1 = Entry(root, textvariable=v1)
entry1.pack()
v1.set("请输入用户名")# 设置默认值
label2 = Label(root, text="密码：")
label2.pack()
v2 = StringVar()
entry2 = Entry(root, textvariable=v2, show="*")
entry2.pack()
Button(root, text="登录", command=confirm).pack()
root.mainloop()
