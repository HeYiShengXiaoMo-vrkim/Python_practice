from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('label的使用方法')
root.geometry('500x500')

#  文本的显示
widget1 = Label(root, text="widget1", width=10, height=1, bg="black", fg="white")
print(widget1.keys())
widget1.pack()

widget2 = Label(root, text="widget2", bg="black", fg="white")#  图片的显示
widget2.pack()

photo = PhotoImage(file="D:\图片\giphy.gif")
widget3 = Label(root, image=photo)
widget3.pack()

# 显示多哦行文本
widget4 = Label(root, text="widget4第一行 '\n'widget4第二行 '\n'widget4第三行", width=10, height=1, borderwidth=1, relief="solid", justify="right", bg="black", fg="white")
widget4.pack()

root.mainloop()