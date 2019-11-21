#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术

import ipaddress,multiprocessing,threading,queue,ntplib
import struct,pprint
# from kamene.all import *
from pyx import *
import time,datetime
import os,random

from netmiko import ConnectHandler
from multiprocessing import Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support


#--------------------------------scapy---------------------------------
# pp = pprint.PrettyPrinter(indent=4)
# # for x , y in ifaces.items():
# #     pp.pprint(x , y)
# pp.pprint(ifaces)

# from kamene.all import *
# p = IP(dst = 'www.somesite.ex') / TCP(dport = 80) / Raw(b'Some raw bytes')
# # to see packet content as bytes use bytes(p) not str(p)
# sr1(p)

# net = ipaddress.ip_network('192.168.100.0/24')
# # 空列表，存放
# ip_list = []
# for ip in net:
#     ip_list.append(str(ip))  # ip格式转为str，放入ip_list
# print(ip_list)

#--------------------------------单任务---------------------------------
# def print_hello(arg):
#     t_start = time.time()
#     print("({})进程开始执行，进程号为{}，线程号为{}".format(arg, os.getpid(), threading.current_thread().getName()))
#     time.sleep(random.random() * 2)
#     t_stop = time.time()
#     print("  >>>({})进程执行完毕，耗时{:0.2f}".format(arg, t_stop - t_start))
# if __name__ == '__main__':
#     t_start = time.time()
#     for i in range(10):
#         print_hello(i)
#     t_stop = time.time()
#
#     print("总耗时：{:0.2f}".format(t_stop-t_start))
#--------------------------------多线程---------------------------------
# def print_hello(arg):
#     t_start = time.time()
#     print("({})任务开始执行，进程号为{}，线程号为{}".format(arg, os.getpid(), threading.current_thread().getName()))
#     time.sleep(random.random() * 2)
#     t_stop = time.time()
#     print("  >>>({})任务执行完毕，耗时{:0.2f}".format(arg, t_stop - t_start))
# if __name__ == '__main__':
#     t_start = time.time()
#     threads = []
#     for i in range(10):
#         task = threading.Thread(target=print_hello,args=(i,))
#         threads.append(task)
#
#     for t in threads:
#         t.start()
#         t.join()
#
#     t_stop = time.time()
#
#     print("总耗时：{:0.2f}".format(t_stop-t_start))

#--------------------------------多进程---------------------------------
# def print_hello(arg):
#     t_start = time.time()
#     print("({})任务开始执行，进程号为{}，线程号为{}".format(arg, os.getpid(), threading.current_thread().getName()))
#     time.sleep(random.random() * 2)
#     t_stop = time.time()
#     print("  >>>({})任务执行完毕，耗时{:0.2f}".format(arg, t_stop - t_start))
# if __name__ == '__main__':
#     t_start = time.time()
#     process = []
#     for i in range(10):
#         task = multiprocessing.Process(target=print_hello,args=(i,))
#         process.append(task)
#
#     for t in process:
#         t.start()
#         t.join()
#
#     t_stop = time.time()
#
#     print("总耗时：{:0.2f}".format(t_stop-t_start))
#--------------------------------多进程/多线程池---------------------------------
# def print_hello(arg):
#         # t_start = time.time()
#         # print("({})进程开始执行，进程号为{}".format(arg,os.getpid()))
#         # time.sleep(random.random() * 2)
#         # t_stop = time.time()
#         # print("...({})进程执行完毕，耗时{:0.2f}".format(arg, t_stop - t_start))
#
#         t_start = time.time()
#         print("({})线程开始执行，进程号为{}，线程号为{}".format(arg,os.getpid(),threading.current_thread().getName()))
#         time.sleep(random.random() * 2)
#         t_stop = time.time()
#         print("...({})线程执行完毕，耗时{:0.2f}".format(arg, t_stop - t_start))
#
# if __name__ == '__main__':
#     # for i in range(10):
#     #     print_hello(i)
#     freeze_support()
#     # 多进程
#     # pool = ProcessPool(processes=4)  # 并发数，缺省为内核数
#
#     # 多线程
#     pool = ThreadPool(processes=5)
#
#     for i in range(8):
#         pool.apply_async(print_hello,args=(i,))
#
#     pool.close()
#     pool.join()

#-----------------------------------------------------------------
# q = queue.Queue()
#
# q_put = []
# q_get = []
#
# for i in range(3):
#     q_result = q.put(i)
#     q_put.append(q_result)
#
# while not q.empty():
#     q_get.append(q.get(i))
#
# print("put队列：",q_put)
# print("get队列：",q_get)

#only unix/linux/mac
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# print('fork是： ', pid)
# if pid == 0:
#     print('I am child process (%s) and my parant is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

#--------------------------------进程---------------------------------
# def run(name):
#     print("子进程 {} ({})".format(name, os.getpid()))
#
# if __name__ == "__main__":
#     print("父进程 {}".format(os.getpid()))
#     p = Process(target=run, args=('test',))
#     print("子进程开始...")
#     p.start()
#     p.join()
#     print("子进程结束.")
#--------------------------------进程间通信---------------------------------

# def write(q):
#   write_data = ['icmp','arp','tcp','udp']
#   for x in write_data:
#     q.put(x)
#
# def read(q):
#     read_date = list()
#     while True:
#         data = q.get()
#         read_date.append(data)
#         if q.empty():
#             break
#     print('数据已经读取完毕:\n',read_date)
#
# def main():
#  q = multiprocessing.Queue()
#  p1 = multiprocessing.Process(target=write,args=(q,))
#  p2 = multiprocessing.Process(target=read,args=(q,))
#  p1.start()
#  p2.start()
#  p1.join()
#  p2.terminate()
#
# if __name__ == '__main__':
#     main()

#--------------------------------进程池---------------------------------
# def run(msg):
#     t_start = time.time()
#     print("({})进程开始执行，进程号为{}".format(msg,os.getpid()))
#     time.sleep(random.random() * 2)
#     t_stop = time.time()
#     print("...({})进程执行完毕，耗时{:0.2f}".format(msg, t_stop - t_start))
#
# if __name__ == '__main__':
#     p = multiprocessing.Pool(3)
#     for i in range(0,6):
#         p.apply_async(run, args=(i,))
#     print('-'*10,'start','-'*10)
#     p.close()
#     p.join()
#     print('-'*10,'stop','-'*10)


# def run():
#     ssh = ConnectHandler(device_type='cisco_ios', host='192.168.0.101', username='cisco', password='cisco', secret='cisco')
#     ssh.enable()
#     reply = ssh.find_prompt()
#     print('>' * 10 + '成功登陆并获取提示符如下:' + '>' * 10 + '\n' + reply)
#
#     r = ssh.send_command('show ip int br')
#     time.sleep(2)
#     print('>' * 10 + ' 命令执行结果如下:' + '>' * 10 + '\n' + r)
#
#     ssh.disconnect()

# if __name__ == '__main__':
#     run()

# c = ntplib.NTPClient()
# r = c.request('0.cn.pool.ntp.org')
# t = r.tx_time
#
# print('<往返延迟>：',r.delay)
# print('<offset>：',r.offset)
# print('<目标时间戳>：',datetime.datetime.fromtimestamp(r.dest_time))
# print('<原始时间戳>：',datetime.datetime.fromtimestamp(r.orig_time))
# print('<接受时间戳>：',datetime.datetime.fromtimestamp(r.recv_time))
# print('<基准时间戳>：',datetime.datetime.fromtimestamp(r.ref_time))
# print('<发送时间戳>：',datetime.datetime.fromtimestamp(r.tx_time))
# _date,_time = str(datetime.datetime.fromtimestamp(t))[:21].split(' ')
# print('标准时间：' , _date,_time)


'''自动修改本地时间
import os
import sys
import time
import ntplib
from ctypes import *
import platform

# 判断获取权限
def running_as_admin(fun):

    if ctypes.windll.shell32.IsUserAnAdmin():
        pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    fun()

# 获取并设置系统时间
def get_NTP_time():

    # import pdb; pdb.set_trace()

    c = ntplib.NTPClient()

    while True:

        try:
            response = c.request('pool.ntp.org')
            ts = response.tx_time
            _date = time.strftime('%Y-%m-%d',time.localtime(ts))
            _time = time.strftime('%X',time.localtime(ts))

            os.system('date {} && time {}'.format(_date,_time))

            return

        except:
            time.sleep(6)

if __name__ == '__main__':

    if 'Windows' == platform.system():

        # 隐藏dos窗口
        whnd = ctypes.windll.kernel32.GetConsoleWindow()
        if whnd != 0:
            ctypes.windll.user32.ShowWindow(whnd, 0)
            ctypes.windll.kernel32.CloseHandle(whnd)

        running_as_admin(get_NTP_time())

    else:
        print("worked under windows only")
'''



