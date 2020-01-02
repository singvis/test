#!/usr/bin/env python
#coding:utf-8
#欢迎关注微信公众号：点滴技术
#这里有靠谱的、有价值的、共成长的，专属于网络攻城狮

import paramiko, time
from paramiko.ssh_exception import NoValidConnectionsError,AuthenticationException

#第一种方法：
def ssh_client(host, user, pwd, cmds, verbose=True):
    '''
    Ubuntu操作步骤：
    1)ssh-keygen生成密钥对；
    2）vi /etc/ssh/sshd_config  //编辑
        PubkeyAuthentication yes   //开启
        AuthorizedKeysFile .ssh/authorized_keys    //开启
    3）把securityCRT生成的公钥copy到authorized_keys
    4）/etc/init.d/ssh restart重启服务
    '''
    # 私钥文件的存放路径
    # private = paramiko.RSAKey.from_private_key_file(r'C:\Users\singvis\Documents\Identity')
    # 创建一个实例化
    ssh = paramiko.SSHClient()
    # 加载系统SSH密钥
    ssh.load_system_host_keys()
    # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不在本地knows_hosts文件中记录的主机将无法连接，默认拒接
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接设备
    try:
        ssh.connect(hostname=host,
                    username=user,
                    # timeout=5,
                    # compress=True,
                    password=pwd
                    #pkey=private,
                    )

        print("正在连接主机{}.....".format(host))
    except NoValidConnectionsError:
        print('连接出现了问题')
    except AuthenticationException:
        print('用户名或密码错误')
    except Exception as e:
        print('其他错误问题{}'.format(e))
    finally:
        #激活交互式shell
        chan = ssh.invoke_shell()
        time.sleep(1)

        for cmd in cmds:
            chan.send(cmd.encode())
            #一定要有回车'Enter'这个动作
            chan.send(b'\n')
            time.sleep(2)
            r = chan.recv(40960).decode()
            if verbose:
                print(r)
        chan.close()
        ssh.close()

#第二种方法：transport方式
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

def sftp_get(ip, user, pwd, local_file,remote_file, port=22):
    try:
        #创建一个实例化
        # ssh = paramiko.SSHClient()
        #加载系统SSH密钥
        # ssh.load_system_host_keys()
        #自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不在本地knows_hosts文件中记录的主机将无法连接
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接设备
        # ssh.connect(ip, port, user, pwd)
        # sftp = ssh.open_sftp()
        # if os.path.isfile(local_file) == False:
        #     with open(local_file,'w') as f:
        #         pass
        # sftp.get(remote_file, local_file)

        t = paramiko.Transport(ip, port)
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remote_file, local_file)
        t.close()

    except Exception as e:
        print(e)


def sftp_put(ip, user, pwd, local_file, remote_file, port=22):
    try:
        t = paramiko.Transport(ip, port)
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_file, remote_file)
        t.close()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    '''
    不要运行的，请注释掉，前面加'#'符号
    '''
    ip = '192.168.0.101'
    user= 'admin'
    pwd= 'Admin@123'
    # local_file = r'D:\test\123.txt'
    # remote_file = 'flash:/vrpcfg.zip'
    # sftp_get(ip='192.168.0.200', user=user, pwd=pwd, remote_file=remote_file, local_file=r'D:\test\vrpcfg.zip')
    # sftp_put(ip='192.168.0.200', user=user, pwd=pwd, local_file=local_file, remote_file='flash:/123.txt')

    cmds = ['terminal length 0', 'show version', 'show ip int br','show ip route']
    # cmds = ['disp ip int br','disp device','disp clock']
    ssh_client(ip, user, pwd, cmds)




