#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

# 尝试用psutil库，psutil.net_if_addrs()一行代码获取所有的网卡信息。

import platform

def get_ifname(ifname):
    if platform.system() == "Linux":
        return ifname
    elif platform.system() == "Windows":
        from Tools.Win_get_key import get_key
        return get_key(ifname)
    else:
        return None

if __name__ == "__main__":
    #适用与Windows、Linux，获取网络接口卡或key
    # print(get_ifname('ens32'))
    print(get_ifname('WLAN'))