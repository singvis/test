import ipaddress
import platform
import pprint
import netifaces
import winreg


# net = ipaddress.ip_network('192.168.1.0/29')
# print('总共多少个地址: ' + str(net.num_addresses))
#
# print('\n' + '-'*20 + '所有地址明细如下：' + '-'*20)
# for ip in net:
#     print(ip)
# print('-'*20 + '-'*20)
#
# a = ipaddress.ip_network('192.168.0.1')
# result = a in net
# print('\n是否在IP段里面：' + str(result))

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(netifaces.interfaces())
# pp.pprint(netifaces.ifaddresses('{CD94297B-D746-4494-91F7-3E40C091A0FC}')[netifaces.AF_INET][0]['addr'])
