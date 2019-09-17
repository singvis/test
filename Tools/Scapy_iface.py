#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的


import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *
from Win_get_key import get_key
import platform


def scapy_iface(ifname):
    if platform.system() == "Linux":
        return ifname
    elif platform.system() == "Windows":
        for x, y in ifaces.items():
            # print(x, y)
            if y.pcap_name is not None:
                # print(y.pcap_name)
                if get_key(ifname) == ('{' + y.pcap_name.split('{')[1]):
                    return x
                else:
                    pass


if __name__ == '__main__':
    # print(ifaces)
    print(scapy_iface('WLAN'))