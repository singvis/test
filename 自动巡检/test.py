#!/usr/bin/env python3
#-*- coding:UTF-8 -*-
#欢迎关注微信公众号：点滴技术
#这里有靠谱、有价值的、免费分享、成长的，专属于网络攻城狮的

from netmiko import ConnectHandler
import os
import time
import threading
import queue

DEVICES_INFO_PATH = 'DEVICES.cfg'
LOG_PATH = 'LOG'
THREADING_NUM = 10
# The number of threading
CMD_DELAY = 1
# sleep time
Q = queue.Queue(THREADING_NUM)
# FIFO
queueLock = threading.Lock()




def show_info(msg):
    queueLock.acquire()
    print(msg)
    queueLock.release()

def get_devices_info():
    try:
        with open(DEVICES_INFO_PATH, 'r') as f:
            for line in f:
                if len(line) == 1:
                    # ignore blank line (len('\n')==1)
                    continue
                info_line = line.split()
                # print(info_line)
                # using whitespace as the delimiter string(leading and trailing whitespace removed)
                if info_line[0][0] == '#':
                #     # ignore comment line
                    continue
                else:
                    info_dict = {
                        # 'devicename': info_line[0],
                        'ip': info_line[0],
                        'username': info_line[1],
                        'password': info_line[2],
                        'cmd': info_line[3]
                    }
                    print(info_dict)
                    # yield info_dict
    except FileNotFoundError as e:
        show_info('Can not find "{}"'.format(DEVICES_INFO_PATH))
    except IndexError as e:
        show_info('"{}" format error'.format(DEVICES_INFO_PATH))

def get_cmd_info(CMD_Info_Path):
    CMD = []
    DEVICES_TYPE = ''
    try:
        with open(CMD_Info_Path, 'r') as f:
            for line in f:
                if len(line) == 1:
                    continue
                # ignore blank line (len('\n')==1)
                cmd_line = line.strip()
                # leading and trailing whitespace removed
                if cmd_line[0] == '#':
                    continue
                # ignore comment line
                if cmd_line[:12] == 'device_type:':
                    DEVICES_TYPE = cmd_line[12:]
                    # get device_type
                else:
                    CMD.append(cmd_line)
            if DEVICES_TYPE == '':
                raise UnboundLocalError('No Device Type')
            return DEVICES_TYPE, CMD

    except FileNotFoundError as e:
        show_info('Can not find "{}"'.format(CMD_Info_Path))
    except UnboundLocalError as e:
        show_info('Can not find "device_type" in "{}"'.format(CMD_Info_Path))

if __name__ == '__main__':

    get_devices_info()

    # hosts = get_devices_info()
    #
    # try:
    #     for i in hosts:
    #         device_type, commands = get_cmd_info(i['cmd'])
    #
    #
    # except TypeError as e:
    #     show_info('Please check the error.')