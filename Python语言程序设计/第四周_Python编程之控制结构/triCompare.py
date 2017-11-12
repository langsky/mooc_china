# coding=utf-8
# /usr/bin/env python3

import math


# 通盘比较
def main1():
    print("This program finds the biggest numbers of three.\n")
    a, b, c = eval((input("Please input the three numbers(a,b,c): ")))
    max_number = 0
    if a >= b and a >= c:
        max_number = a
    if b >= a and b >= c:
        max_number = b
    if c >= a and c >= b:
        max_number = c
    print("%s is the biggest number of the three." % str(max_number))


# 决策树比较
def main2():
    print("This program finds the biggest numbers of three.\n")
    a, b, c = eval((input("Please input the three numbers(a,b,c): ")))
    max_number = 0
    if a >= b:
        if a >= c:
            max_number = a
        else:
            max_number = c
    if b >= a:
        if b >= c:
            max_number = b
        else:
            max_number = c
    print("%s is the biggest number of the three." % str(max_number))


# 顺序比较
def main3():
    print("This program finds the biggest numbers of three.\n")
    a, b, c = eval((input("Please input the three numbers(a,b,c): ")))
    max_number = a
    if b > max_number:
        max_number = b
    if c > max_number:
        max_number = c
    print("%s is the biggest number of the three." % str(max_number))


# python内置函数
def main4():
    print("This program finds the biggest numbers of three.\n")
    a, b, c = eval((input("Please input the three numbers(a,b,c): ")))
    max_number = max(a, b, c)
    print("%s is the biggest number of the three." % str(max_number))
    

if __name__ == '__main__':
    main1()
