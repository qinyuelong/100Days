from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    '''

    # AF_INET  - IPv4
    # AF_INET6 -IPv6
    # SOCK_STREAM -tcp 套接字
    # SOCK_DGRAM - UDP 套接字
    SOCK_RAW - 原始套接字
    :return:
    '''
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 6789))
    server.listen(512)
    print('服务器启动监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '链接到了服务器')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()



if __name__ == '__main__':
    main()