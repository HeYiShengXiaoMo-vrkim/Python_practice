import socket

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 8080))

# 服务器地址
addr = ('192.168.121.1', 8080)

# 输入要发送的信息
data = input("请输入要发送的信息：")

# 发送信息
try:
    s.sendto(data.encode('utf-8'), addr)
    print("信息发送成功！")
except OSError as e:
    print(f"发送失败: {e}")

redata = s.recvfrom(1024) # 本次接受最大字节数
# 关闭套接字
s.close()
