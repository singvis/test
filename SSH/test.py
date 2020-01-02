#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

import paramiko

def ssh_client(cmd_list):
    #私钥的绝对路径
    # private = paramiko.RSAKey.from_private_key_file(r'C:\Users\singvis\Documents\Identity')

    # 创建一个实例化
    ssh = paramiko.SSHClient()

    # t = paramiko.Transport('192.168.0.101', 22)
    # t.connect(username='cisco', password='cisco')
    # ssh._transport = t

    # 加载系统HostKeys密钥
    ssh.load_system_host_keys()
    # 自动添加策略，保存远端主机的主机名和密钥信息，如果不添加，那么不在本地knows_hosts文件中记录的主机将无法连接，默认拒接
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #连接远端主机
    ssh.connect('192.168.0.200',port=22, username='huawei', password='huawei')
    #执行命令
    for cmd in cmd_list:
        stdin, stdout,stderr = ssh.exec_command(cmd)
        print(stdout.read().decode('utf-8'))
    ssh.close()

def sftp_put():
    local_path =r'D:\test\123.txt'
    remote_path ='flash:/123.txt'

    t = paramiko.Transport('192.168.0.200', 22)
    t.connect(username='huawei', password='huawei')
    #
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(local_path,remote_path)
    t.close()

def sftp_get():
    local_path = r'D:\test\vrpcfg.zip'
    remote_path = 'flash:/vrpcfg.zip'

    t = paramiko.Transport('192.168.0.200', 22)
    t.connect(username='huawei', password='huawei')
    #
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remote_path, local_path)
    t.close()





# if __name__ == '__main__':
    # cmd_list = ['disp ip int br','disp device','disp clock']
    # ssh_client(cmd_list=cmd_list)
    # sftp_put()
    # sftp_get()

import paramiko
import time
import sys


def QYT_SSHClient_MultiCMD(ip, username, password, cmd_list, verbose=True):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.load_system_host_keys()  # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # SSH连接

    chan = ssh.invoke_shell()  # 激活交互式shell
    time.sleep(1)

    for cmd in cmd_list:  # 读取命令
        chan.send(cmd.encode())  # 执行命令，注意字串都需要编码为二进制字串
        chan.send(b'\n')  # 一定要注意输入回车
        time.sleep(2)  # 由于有些回显可能过长，所以可以考虑等待更长一些时间
        x = chan.recv(40960).decode()  # 读取回显，有些回想可能过长，请把接收缓存调大
        if verbose:
            print(x)  # 打印回显

    chan.close()  # 退出交互式shell
    ssh.close()  # 退出ssh会话


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    QYT_SSHClient_MultiCMD('192.168.0.200', 'huawei', 'huawei', ['disp ip int br','disp device','disp clock'])