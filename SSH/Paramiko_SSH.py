#!/usr/bin/env python
#coding:utf-8

import paramiko

#第一种方法：
def ssh_client(cmd):
    try:
        #创建一个实例化
        ssh = paramiko.SSHClient()
        #加载系统SSH密钥
        ssh.load_system_host_keys()
        #自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不在本地knows_hosts文件中记录的主机将无法连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接设备
        ssh.connect(hostname='192.168.0.101', port=22, username='cisco', password='cisco',timeout=5,compress=True)
        #执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        #执行结果

        r = stdout.read().decode('utf-8')
        # 关闭SSH
        ssh.close()
        return ("'{}' 的输出结果如下：\n{}".format(cmd,r))


    except Exception as e:
        print(e)
        # print('%stErrorn %s' % (hostname, e))

#第二种方法：
def ssh_transport(cmd):
    try:
        t = paramiko.Transport('192.168.0.101',22)
        t.connect(username='cisco', password='cisco')
        ssh = paramiko.SSHClient()
        ssh._transport = t
        stdin, stdout, stderr = ssh.exec_command(cmd)
        r = stdout.read().decode('utf-8')
        t.close()
        return ("'{}' 的输出结果如下：\n{}".format(cmd,r))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    cmds = ['terminal length 0','show version', 'show ip int br','show ip route']
    for c in cmds:
        # print(ssh_client(cmd=c))
        print(ssh_transport(cmd=c))



