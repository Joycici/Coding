#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 15:Reading file
'''
"""
__author='Joycici'
__version__=' 
"""
# 调用modules
from sys import argv

# unpacking
script, filename = argv
# 打开filename变量传入的文件，将它赋给txt变量
txt = open(filename)
#输出文件名
print "Here'script file %r:" % filename
# 输出文件内容
print txt.read()
# 再次输出文件名
print "Type the filename again:"
# 从交互界面获得文件名，并赋给file_again变量
file_again = raw_input("> ")
# 打开file again 变量传入的文件并赋予txt_again
txt_again = open(file_again)
# 输出txt_again变量内容
print txt_again.read()

# 关闭变量
txt.close()
txt_again.close()
