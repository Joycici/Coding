#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__author='Joycici'
__version__='1.0' 
"""

from sys import argv
script ,first, second, third = argv

print "The script is call'd ", script
print "Your first varialbe is ", first
print "Your second varialbe is ", second
print "Your third variable is ", third

# 没有输入参数或者参数输入数量不对都报下面错误
'''
PS E:\python\Exercise> python .\ex13.py
Traceback (most recent call last):
  File "\.\\ex13.py", line 4, in <module>
    script ,first, second, third = argv
ValueError: need more than 1 value to unpack
'''

# python后面的都是参数

'''
PS E:\python\Exercise> python .\ex13.py
Traceback (most recent call last):
  File "\.\\ex13.py", line 4, in <module>
    script ,first, second, third = argv
ValueError: need more than 1 value to unpack
'''
# 附加题3 Combine raw_input with argv to make a script that gets more input from a user. Don't over think it. 
# Just use argv to get something, and raw_input to get something else from the user.
print "combine raw_input and avgs %r " % raw_input() 
print raw_input("combine raw_input and avgs : ")
abc = raw_input("combine raw_input and avgs : ")
print abc 
# 