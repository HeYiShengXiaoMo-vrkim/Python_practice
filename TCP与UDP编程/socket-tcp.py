"""
! -- TCP工作原理 -- !
TCP服务器 socket() -> bind() -> listen() -> accept() -> recv()/send() -> read()/write() -> close()
                                            |
                          ——————————————————
                         |(accept()阻塞)
                         |TCP三次握手建立连接:客户端发送SYN(同步,包含客户端端口,连接初始序号)给服务器，服务器发送SYN+ACK给客户端(同时TCP序号加一)，客户端发送ACK给服务器(同时TCP序号加一)
TCP客户端 socket() -> connect() -> send()/recv() -> read()/write() -> close()
"""
"""
# 一. TCP创建服务器
import socket

# 1. 创建套接字
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定端口
serverSocket.bind(('127.0.0.1', 9999))

# 3. 监听端口号
serverSocket.listen(128)  # 128为最大连接数

# 4. 等待客户端socket连接 clientSocket为客户端socket，clientAddr为客户端地址以及端口号
clientSocket, clientAddr = serverSocket.accept()  # accept()为阻塞函数，等待客户端连接

# 5. 读取客户端发送的数据
data = clientSocket.recv(1024)  # 1024为最大接收字节数
print(f"接收到客户端 {clientAddr} 的数据: {data.decode('utf-8')}")

# 6. 向客户端发送数据
response = "Hello, client! I received your message."
clientSocket.send(response.encode('utf-8'))

# 7. 关闭套接字
clientSocket.close()
serverSocket.close()
"""


# 二. TCP创建客户端
import socket
# 1. 创建套接字
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器
clientSocket.connect(('192.168.121.1', 8080))
"""
1. 此后已经连接好了服务器(我们是tcp),所以在以后的数据发送过程中,不需要再指定服务器的地址和端口号
2. udp在发送数据时,需要指定服务器的地址和端口号
"""
# 3. 向服务器发送数据
message = "Hello, server! This is a TCP client."
clientSocket.send(message.encode('utf-8'))
# 4. 接收服务器发送的数据
recvData = clientSocket.recv(1024)
print(f"接收到服务器的数据: {recvData.decode('utf-8')}")
# 5. 关闭套接字
clientSocket.close()