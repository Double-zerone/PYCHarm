
### 一服务器多客户端通信
from socket import *  # 服务器端
from threading import Thread

sockets = []  # 保存所有在线客户client_socket


def main():
    # 创建服务器套接字对象
    sever_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口
    sever_socket.bind(('', 8887))
    # 监听
    sever_socket.listen()

    while True:
        # 登待客户端连接
        client_socket, client_info = sever_socket.accept()
        sockets.append(client_socket)
        t = Thread(target=readMsg, args=(client_socket,))
        t.start()


def readMsg(client_socket):
    # 读取客户端消息
    while True:
        recv_data = client_socket.recv(1024)
        if recv_data.decode('utf-8').endswith('bye'):  # 收到bye移除客户端
            sockets.remove(client_socket)
            client_socket.close()
        if len(recv_data) > 0:
            for socket_m in sockets:
                socket_m.send(recv_data)

            # 将消息发给在线客户端
            # print('客户:', recv_data.decode('utf-8'))
            # msg = input('>>>')

            # # 调用send发消息
            # client_socket.send(msg.encode('utf-8'))


if __name__ == "__main__":
    main()
#