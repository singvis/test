#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

import socket

def main():
    # 创建一个套接字对象
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("想要退出，请输入‘Q’或‘q’：")
    print( '-'*20 + "消息窗口" + '-'*20)

    '''接受数据'''
    # 绑定IP和端口
    local_addr = ('', 8888)
    s.bind(local_addr)

    '''发送数据'''

    while True:
        msg = input("请输入你想发的消息： ")
        # # s.sendto(b"Hello world", ("192.168.0.1",8080))
        s.sendto(msg.encode('gbk'), ("192.168.0.133",8080))

        #  接受数据
        # recv_date = s.recvfrom(1024)

        #  打印消息
        # print(recv_date)
        # print("#发送者：{}:\n\t发送的信息：{}".format(recv_date[1],recv_date[0].decode('gbk')))

        # if msg == 'Q':
        #     break
        # elif msg == 'q':
        #     break

    s.close()
if __name__ == '__main__':
    main()