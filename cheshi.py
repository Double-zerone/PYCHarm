
#客户端

from socket import *
from threading import Thread

# 创建客户端套接字对象
client_socket = socket(AF_INET, SOCK_STREAM)
# 调用connect方法和主机服务器连接
client_socket.connect(('192.168.43.194', 8887))
user = input("用户名:")
flsg = True


def readMsg(client_socket):
    global flsg
    while flsg:
        recv_data = client_socket.recv(1024)  #读取消息
        print(recv_data.decode('utf-8'))


def writeMsg(client_socket):
    global flsg
    while flsg:
        # 客户端发消息
        msg = input('>>>')
        msg = user + ':' + msg
        if msg.endswith('bye'):  #以bye结尾
            flsg = False
        # 客户端接受消息
        client_socket.send(msg.encode('utf-8'))
        # recv_data = client_socket.recv(1024)
        # print('服务器:', recv_data.decode('utf-8'))

    # client_socket.close()


# 开启一个线程处理客户端的读取消息

t1 = Thread(target=readMsg, args=(client_socket,))

# 开启一个线程处理客户端的发送消息

t2 = Thread(target=writeMsg, args=(client_socket,))
t1.start()
t2.start()
t1.join()
t2.join()
client_socket.close()


