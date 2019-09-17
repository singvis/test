#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术

from socket import inet_aton
import struct
import  ipaddress

IP_LIST = ['172.16.12.123',
           '172.16.12.3',
           '172.16.12.234',
           '172.16.12.12',
           '172.16.12.23',
           ]

def sort_ip(ips):
    return sorted(ips , key=lambda ip:ipaddress.ip_address(ip))

if __name__ == '__main__':
    print(sort_ip(IP_LIST))