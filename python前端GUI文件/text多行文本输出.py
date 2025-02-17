from tkinter import *
root = Tk()
root.title("多行文本输出")
root.geometry("1400x800")
w1 = Text(root, width=30, height=10)
w1.pack()

w1.insert(1.0, "0123456789\nabcdefg")
w1.insert(2.0, "1234567890\n1234567890")
w1.insert(INSERT, 'I Love')  # 在光标位置插入
w1.insert(END, 'Python')  # 在末尾插入
photo = PhotoImage(file="D:\图片\giphy.gif")

def show():
    print("被点击了")
    w1.image_create(END, image=photo)  # 在末尾插入图片
    # Indexes(索引)是用来指向Text组件中文本的位置，Text的组件索引也是对应实际字符之间的位置
    # 核心：行号以1开始 列号以0开始
    print(w1.get(1.0, END))  # 获取文本内容
    w1.insert(1.8, "gaoqi")  # 在第1行第8列插入文本
    print("所有文本内容：", w1.get(1.0, END))

# text 还可以插入按钮，图片等
b1 = Button(root, text="点击", command=show)
w1.window_create(INSERT, window=b1)  # 在光标位置插入按钮
root.mainloop()