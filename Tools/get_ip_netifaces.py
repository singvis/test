from netifaces import interfaces , ifaddresses ,AF_INET , AF_INET6
import platform

def get_ip_address(ifname):
    if platform.system() == "linux":
        return ifaddresses(ifname)[AF_INET][0]['addr']
    elif platform.system() == "Windows":
        from Tools.WIN_IFNAME import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        return ifaddresses(if_id)[AF_INET][0]['addr']
    else:
        print('该操作系统不支持，本脚本只能工作再Windows或者linux环境下')

def get_ipv6_address(ifname):
    if platform.system() == "linux":
        return ifaddresses(ifname)[AF_INET6][0]['addr']
    elif platform.system() == "Windows":
        from Tools.WIN_IFNAME import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        return ifaddresses(if_id)[AF_INET6][0]['addr']
    else:
        print('该操作系统不支持，本脚本只能工作再Windows或者linux环境下')

if __name__ == '__main__':
    print('你的ipv4地址是：' + get_ip_address('WLAN'))
    print('你的ipv6地址是：' + get_ipv6_address('WLAN'))
    # print(get_ip_address('ens32'))
    # print(get_ipv6_address('ens32'))