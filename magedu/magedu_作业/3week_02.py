#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

import random
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