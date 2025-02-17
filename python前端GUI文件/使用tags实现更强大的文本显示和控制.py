from tkinter import *
import webbrowser

# 创建主窗口
root = Tk()
root.title('使用tags实现更强大的文本显示和控制')
root.geometry('600x400')

# 创建一个文本框
text_box = Text(root, width=50, height=20)
text_box.pack()

# 在文本框中插入文本
text_box.insert(INSERT, 'hello world\n你好世界！\n百度一下，你就知道。')

# 创建一个标签
# tag_add()方法用于在文本框中添加一个标签，参数1是标签的名称，参数2和参数3是标签作用的文本范围
red_text_tag = text_box.tag_add('tag1', '1.0', '1.11')
green_text_tag = text_box.tag_add('tag2', '2.0', '2.5')
baidu_text_tag = text_box.tag_add('baidu', '3.0', '3.10')

# 设置标签的属性
# tag_config()方法用于设置标签的属性，参数1是标签的名称，参数2是属性名称，参数3是属性值
text_box.tag_config('tag1', foreground='red', font=('Arial', 20, 'bold'))
text_box.tag_config('tag2', foreground='green', font=('Arial', 20, 'bold'))
text_box.tag_config('baidu', foreground='blue',  font=('Arial', 20, 'bold'), underline=True)
# tag_bind()方法用于绑定标签的事件，参数1是标签的名称，参数2是事件名称，参数3是事件处理函数
text_box.tag_bind('baidu', '<Button-1>', lambda event: webbrowser.open('https://www.baidu.com'))

# 运行主循环
root.mainloop()
