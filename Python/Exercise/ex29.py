#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 29: What If
'''
"""
__author='Joycici'
__version__='1.0' 
"""

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people == dogs:
    print "People are dogs."
# 附加题
'''
1. 如果if为真，则执行下一行缩进的代码
2. 为什么要缩进，IF最后的： 告诉python要创建一个新的代码块，缩进后的代码表示自己属于新的代码块
3. 如果不缩进会报错，应为： 后面要求必须有缩进
4. 判断真假的都可以放在if后面
5. 会输出不同的值呀
'''

if True and False:
    print "return false"
if True or False:
    print "return true"