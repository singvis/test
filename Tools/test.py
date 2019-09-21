#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术

import struct
import ipaddress
import pprint
from kamene.all import *


# pp = pprint.PrettyPrinter(indent=4)
# # for x , y in ifaces.items():
# #     pp.pprint(x , y)
# pp.pprint(ifaces)

# from kamene.all import *
# p = IP(dst = 'www.somesite.ex') / TCP(dport = 80) / Raw(b'Some raw bytes')
# # to see packet content as bytes use bytes(p) not str(p)
# sr1(p)

net = ipaddress.ip_network('192.168.1.0/29')
for x in net:
    print(str(x))