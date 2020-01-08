import ipaddress
import platform
import pprint
import netifaces
import winreg
import time,random


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




#------------------------------------------------------第三周作业01：
#随机生成20个整数（1~20）
lst_int = [random.randint(1,20) for x in range(20)]
print(">>> 随机生成20个整数: {}".format(lst_int))
dict_time = {}
for x in lst_int:
    if x in dict_time:
        dict_time[x] = dict_time[x] + 1
    else:
        dict_time[x]=1
print(">>> 统计每个数字出现的次数(左为数字：右为次数): {}".format(dict_time))

new_list = sorted(dict_time.items(),key=lambda x:x[1],reverse=True)

print(">>> 次数出现最多的前三个数字:{}".format(new_list[:3]))


