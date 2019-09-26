#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的。

import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *
from Tools.Get_address import get_ip_address  # 获取本机IP地址
from Tools.Get_address import get_mac_address  # 获取本机MAC地址
from Tools.Scapy_iface import scapy_iface  # 获取scapy iface的名字


def arp_request(dst_addr, ifname):
    # 获取本机IP地址
    local_ip = get_ip_address(ifname)
    # 获取本机MAC地址
    local_mac = get_mac_address(ifname)
    try:  # 发送ARP请求并等待响应
        result_raw = sr1(ARP(op=1,
                             hwsrc=local_mac,
                             hwdst='00:00:00:00:00:00',
                             psrc=local_ip,
                             pdst=dst_addr),
                         iface=scapy_iface(ifname),
                         timeout=1,
                         verbose=False)
        # print(result_raw.show())
        return dst_addr, result_raw.getlayer(ARP).fields.get('hwsrc')

    except AttributeError:
        return dst_addr, None


if __name__ == "__main__":
    # Windows Linux均可使用
    # arp_result = arp_request('192.168.100.1', "WLAN")
    arp_result = arp_request('192.168.8.254', "ens32")
    print("IP地址:", arp_result[0], "MAC地址:", arp_result[1])
