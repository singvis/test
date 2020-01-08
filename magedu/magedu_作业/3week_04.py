#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

import random

str = 'abcdefghijklmnopqrstuvwxyz'

str_list = []
for x in range(100):
    s = random.sample(str, k=2)
    str_list.append(s)
print(">>> 100个组合:{}".format(str_list))



# list_sum = len(str_list)
# print(list_sum)

new_list1 = sorted(str_list,key=lambda x:x[0],reverse=True)
new_list2 = sorted(new_list1,key=lambda x:x[1],reverse=True)
#
print(">>> 降序后的100个组合:{}".format(new_list2))

# new_set = set(new_list2)
#
# print(new_set)
# print(len(new_set))

