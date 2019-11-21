#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

import paramiko , os

def sftp_get(ip, user, pwd,local_file, remote_file, port=22):
    try:
        #创建一个实例化
        ssh = paramiko.SSHClient()
        #加载系统SSH密钥
        ssh.load_system_host_keys()
        #自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不在本地knows_hosts文件中记录的主机将无法连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接设备
        ssh.connect(ip, port, user, pwd)
        sftp = ssh.open_sftp()
        if os.path.isfile(remote_file) == False:
            with open(remote_file,'w') as f:
                pass
        sftp.get(remote_file, local_file)

    except Exception as e:
        pass


def sftp_put(ip, user, pwd, local_file, remote_file, port=22):
    try:
        #创建一个实例化
        ssh = paramiko.SSHClient()
        #加载系统SSH密钥
        ssh.load_system_host_keys()
        #自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不在本地knows_hosts文件中记录的主机将无法连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接设备
        ssh.connect(ip, port, user, pwd)
        sftp = ssh.open_sftp()
        if os.path.isfile(local_file) == False:
            with open(local_file,'w') as f:
                pass
        sftp.put(local_file, remote_file)

    except Exception as e:
        pass

if __name__ == '__main__':
    local_file = 'put_test.txt'
    remote_file = '/tmp/get_test.txt'
    sftp_get('192.168.8.128', 'root', 'lsh@123', remote_file, 'get_test.txt', port=22)
    # sftp_put('192.168.0.254', 'root', 'eve', local_file, '/tmp/put_test.txt', port=22)