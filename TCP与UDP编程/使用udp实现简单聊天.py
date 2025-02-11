import socket
import threading

# 创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
udp_socket.bind(('127.0.0.1', 9999))

def recv(addr):
    while True:
        data = input("请输入要发送的信息：")
        udp_socket.sendto(data.encode('utf-8'), addr)
        redata = udp_socket.recvfrom(1024) # 本次接受最大字节数
        print("收到的信息：",redata.decode('utf-8'))

if __name__ == '__main__':
    p1 = threading.Thread(target=recv, args=('127.0.0.1', 9999))
    p2 = threading.Thread(target=recv, args=('127.0.3.1', 9999))
    p1.start()
    p2.start()
    p1.join()
    p2.join()