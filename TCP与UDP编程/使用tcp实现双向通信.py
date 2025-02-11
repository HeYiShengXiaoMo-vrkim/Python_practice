"""
双向通信socket服务器端
    读取客户端发送的数据，将内容输出到控制台
    将控制台输入的信息发送给客户端
"""
"""
# 导入socket模块
import socket

from python_from_the_beginning.socket网络编程.双向通信socket服务端 import tcpServerSocket

# 创建socket对象
tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
tcpServerSocket.bind('192.168.121.1', 8888)
# 监听端口
tcpServerSocket.listen(128)
# 接受客户端连接
clientSocket, clientAddr = tcpServerSocket.accept()
while True:
    # 读取客户端发送的数据
    data = clientSocket.recv(1024).decode('utf-8')
    # 将内容输出到控制台
    print(f'接收到客户端 {clientAddr} 的数据: {data}')
    if data == 'exit':
        break
    # 将控制台输入的信息发送给客户端
    sendData = input('请输入要发送的信息: ')
    clientSocket.send(sendData.encode('utf-8'))
# 关闭套接字
clientSocket.close()
tcpServerSocket.close()
"""

"""
双向通信socket客户端
    从控制台读取信息，发送给服务器
    从服务器读取信息，输出到控制台
"""
#导入socket模块
import socket
#创建socket对象
tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#连接服务器
tcpClientSocket.connect(('192.168.121.1', 8888))
while True:
    #从控制台读取信息
    sendData = input('请输入要发送的信息: ')
    if sendData == 'exit':
        break
    #发送给服务器
    tcpClientSocket.send(sendData.encode('utf-8'))
    data = tcpClientSocket.recv(1024).decode('utf-8')
    print(data)

#关闭套接字
tcpClientSocket.close()