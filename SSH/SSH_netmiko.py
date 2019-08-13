#coding:utf-8
'''
参考链接：https://pynet.twb-tech.com/blog/automation/netmiko.html
'''

from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from datetime import datetime
import time
import logging

from my_devices import device_list as devices

'定义类'
class SSH_Client():
    '定义login_host函数，用于登陆设备'
    def login_host(self , a_device):
        try:
            self.ssh = ConnectHandler(**a_device)
            self.ssh.enable()
            reply = self.ssh.find_prompt()
            print('>' * 10 + '成功登陆并获取提示符如下:' + '>' * 10 + '\n' + reply)
            return True
        except ValueError:
            logging.warning(a_device['host'] + ' Secret 密码错误')
        except NetMikoTimeoutException:
            logging.warning(a_device['host'] + ' 连接不上设备,请检查网络是否正常通信')
        except NetMikoAuthenticationException:
            logging.warning(a_device['host'] + ' 登陆失败，用户名或密码错误')

    '定义do_cmd函数,用于执行命令'
    def do_cmd(self,cmds):
        '读取文件，for语句循环执行命令'
        with open(cmds) as cmd_obj:
            for cmd in cmd_obj:
                reply = self.ssh.send_command(cmd)
                time.sleep(2)
                logging.warning('>' * 10 + cmd.rstrip() + ' 命令执行结果如下:' + '>' * 10 + '\n' + reply)
    '定义logout_host函数，关闭程序'
    def logout_host(self):
        self.ssh.disconnect()

if __name__ == '__main__':
    cmds = 'cmd.txt'  # 存放执行命令文件，相对路径
    ssh_client = SSH_Client()
    start_time = datetime.now()
    for a_device in devices:
        '如果登录结果为True，则执行命令，然后退出'
        if ssh_client.login_host(a_device):
            ssh_client.do_cmd(cmds)
            ssh_client.logout_host()
            time.sleep(2)
    stop_time = datetime.now()
    print('总花费时长：{0}\n'.format(stop_time - start_time))
