#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

from __future__ import print_function
import sys
import nmap
import pprint
import time

start_time = time.time()
pp = pprint.PrettyPrinter(4)
nm = nmap.PortScanner()
r = nm.scan('192.168.1.101-103', '22,23')
end_time = time.time()
pp.pprint(r)

print('-'*100)

print("所有主机清单：" + str(nm.all_hosts()))
print("命令行格式： " + nm.command_line())
print("主机的状态： " + nm['192.168.1.101'].state())
print("所有协议：" + str(nm['192.168.1.101'].all_protocols()))
print("所有端口：" + str(nm['192.168.1.101']['tcp'].keys()))
print("22端口状态：" + str(nm['192.168.1.101']['tcp'][22]['state']))
print("23端口状态：" + str(nm['192.168.1.101']['tcp'][23]['state']))

print('-'*100)

print("扫描总花费时间：%.2f" % (end_time-start_time))