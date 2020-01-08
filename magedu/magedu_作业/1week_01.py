#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

#九九乘法表
for i in range(1,10):  #i作为第二个乘数
    for j in range(1,i+1):  #j作为第1个乘数
            print("{} x {} = {}\t".format(j, i, j*i), end='')
    print()