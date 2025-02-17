from tkinter import *
from tkinter import messagebox

def sentFlower():
    messagebox.showinfo(title='提示', message='送你一朵小红花')
    print("送你一朵小红花")

if __name__ == '__main__':
    # 创建主窗口
    root = Tk()
    # 设置窗口标题
    root.title('送你一朵小红花')
    # 设置窗口大小
    root.geometry('300x200')
    # 创建按钮
    btn = Button(root, text='送花', command=sentFlower, width=10, height=2)
    # 将按钮添加到窗口中
    btn.pack()
    # 进入消息循环
    root.mainloop()