#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术

from netifaces import  ifaddresses ,AF_INET , AF_INET6 , AF_LINK,AF_PACKET
import platform



#定义获取ipv4信息的函数
def get_ip_address(ifname):
    #判断系统是否为Linux
    if platform.system() == "Linux":
        try:
            #返回ipv4地址信息
            return ifaddresses(ifname)[AF_INET][0]['addr']
        except ValueError:
            return None
    #判断是否为Windows系统
    elif platform.system() == "Windows":
        #调用函数get_key，获取到了网卡的键值
        from Tools.Win_get_key import get_key
        key = get_key(ifname)
        if not key:
            return
        else:
            #返回ipv4地址信息
            return ifaddresses(key)[AF_INET][0]['addr']
    # 判断是否为Windows系统
    elif platform.system() == 'MacOS':
        pass
    else:
        print('您的系统本程序暂时不支持，目前只支持Linux、Windows、MacOS')

def get_mac_address(ifname):
    #判断系统是否为Linux
    if platform.system() == "Linux":
        try:
            #返回ipv4地址信息
            return ifaddresses(ifname)[AF_PACKET][0]['addr']
        except ValueError:
            return None
    #判断是否为Windows系统
    elif platform.system() == "Windows":
        #调用函数get_key，获取到了网卡的键值
        from Tools.Win_get_key import get_key
        key = get_key(ifname)
        if not key:
            return
        else:
            #返回ipv4地址信息
            return ifaddresses(key)[AF_LINK][0]['addr']
    # 判断是否为Windows系统
    elif platform.system() == 'MacOS':
        pass
    else:
        print('您的系统本程序暂时不支持，目前只支持Linux、Windows、MacOS')

#定义获取ipv6信息的函数，与上面函数大体一致，不备注
def get_ipv6_address(ifname):
    if platform.system() == "Linux":
        try:
         return ifaddresses(ifname)[AF_INET6][0]['addr']
        except ValueError:
            return None
    elif platform.system() == "Windows":
        from Tools.Win_get_key import get_key
        key = get_key(ifname)
        if not key:
            return
        else:
           return ifaddresses(key)[AF_INET6][0]['addr']
    elif platform.system() == 'MacOS':
        pass
    else:
        print('您的系统本程序暂时不支持，目前只支持Linux、Windows、MacOS')

if __name__ == '__main__':
    # print('你的ipv4地址是：' + get_ip_address('WLAN'))
    # print('你的MAC地址是：' + get_mac_address('WLAN'))
    # print('你的ipv6地址是：' + get_ipv6_address('WLAN'))
    print('你的ipv4地址是：' + get_ip_address('ens32'))
    print('你的MAC地址是：' + get_mac_address('ens32'))
    # print('你的ipv6地址是：' + get_ipv6_address('ens32'))
    # print('你的MAC地址是：' + get_mac_address('ens32'))