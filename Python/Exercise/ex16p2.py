#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 16:Reading and writing Files
'''
"""
__author='Joycici'
__version__='1.0' 
"""

'''
附加题2 读刚刚创建的文件
'''
from sys import argv

script,filename = argv

print "Open the filename %r " % filename
txt = open(filename)

print txt.read()

txt.close()
