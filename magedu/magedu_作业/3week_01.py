#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

new_lst = []
lst = [1,4,9,16,2,5,10,15]
for i in range(len(lst) - 1):
        new_lst.append(lst[i]+lst[i+1])

print(new_lst)