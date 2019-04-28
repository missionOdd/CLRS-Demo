# -*- coding:utf-8 -*-
__author__ = 'Missionary'
__time__ = '2019/4/28 0028 12:36'

def fact(n):
    if(n==1):
        return 1
    elif(n>1):
        return n*fact(n-1)
    else:
        raise RuntimeError("负数没有阶乘")

print(fact(4))