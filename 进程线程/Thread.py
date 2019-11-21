#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from netmiko import ConnectHandler
from my_devices import device_list as devices
import threading
import time

class SSH_Client(threading.Thread):
    def __init__(self,ip,cmds):
        threading.Thread.__init__(self)
        self.ip = ip
        self.cmds = cmds

    def login_host(self):
        self.ssh = ConnectHandler(device_type='cisco_ios', host=self.ip, username='cisco', password='cisco',secret='cisco')
        self.ssh.enable()
        reply = self.ssh.find_prompt()
        print('>' * 10 + '成功登陆并获取提示符如下:' + '>' * 10 + '\n' + reply)

    def do_cmd(self):
        for cmd in self.cmds:
            r = self.ssh.send_command(cmd)
            time.sleep(2)
            print('>' * 10 + cmd.rstrip() + ' 命令执行结果如下:' + '>' * 10 + '\n' + r)

    def logout_host(self):
        self.ssh.disconnect()

if __name__ == '__main__':
    cmds = ['show version','show ip int br']
    ips = ['192.168.0.101','192.168.0.102','192.168.0.103','192.168.0.104',]
    start_time = time.time()
    threads = []
    for ip in ips:
        task = SSH_Client(ip,cmds)
        threads.append(task)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print("总共花费时间：{:0.2f}".format(end_time-start_time))