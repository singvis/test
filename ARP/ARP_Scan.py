#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
import ipaddress
from multiprocessing.pool import ThreadPool     #多线程
from ARP_Request import arp_request     #返回ip+mac


def arp_scan(network,ifname):
    net = ipaddress.ip_network(network , strict=False)
    ip_list = []
    for ip in net:
        ip_list.append(str(ip))     #ip格式转为str，放入ip_list
    # print(ip_list)
    pool = ThreadPool(processes=100)    #线程池并发100
    result = []
    for i in ip_list:
        result.append(pool.apply_async(arp_request , args=(i,ifname)))
    pool.close()
    pool.join()
    scan_dict = {}

    # print(result)

    for r in result:
        if r.get()[1] is not None:
            scan_dict[r.get()[0]] = r.get()[1]
    # print(scan_dict)
    return scan_dict

if __name__ == '__main__':
    net = '192.168.100.0/24'
    name = 'WLAN'
    import time
    start_time = time.time()
    print("活动IP地址如下：")
    for ip , mac in arp_scan(network=net,ifname=name).items():
        print("IP地址： {} 是活动的，MAC地址是 {}".format(ip , mac))
    end_time = time.time()
    print('本次扫描花费时间：%.2f' % (end_time - start_time))
