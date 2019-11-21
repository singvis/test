#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的


import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *
from Tools.Get_ifname import get_ifname
import platform


def scapy_iface(ifname):
    if platform.system() == "Linux":
        return ifname
    elif platform.system() == "Windows":
        #ifaces：字典组合，所有网络接口卡名称+相关信息（IP地址/MAC地址/pcap_name/description）
        for x, y in ifaces.items():
            #输出所有网络接口卡信息：如{'网卡名称': <NetworkInterface: 网卡名称 IP地址 MAC地址 pcap_name=... description=网卡名称>}
            #print(ifaces)
            #输出键，值
            #print(x, y)

            #lo0是为None的
            if y.pcap_name is not None:
                #比较key是否一样，一样则返回网络接口卡名称(型号)
                if get_ifname(ifname) == ('{' + y.pcap_name.split('{')[1]):
                    return x
                else:
                    pass


if __name__ == '__main__':
    #适用Windows、Linux
    # print(ifaces)
    print(scapy_iface('WLAN'))