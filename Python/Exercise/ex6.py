#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
__author='Joycici'
__version__='1.0' 
"""

# 输出有10类人
x = "There are %d types of people." % 10
# 定义变量二进制
binary = "binary"
# 定义变量
do_not = "don't"
# 定义变量y 代入上面两个变量输出到屏幕
y = "Those who know %s and those who %s" % (binary, do_not)

# 输出x,y
print x
print y 

# 输出x 
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# 用两个变量输出字符串，其中%hilarious代入joke_evaluation的%r 
# %r输出变量原本的形式
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."
# 拼接两个字符串
print w + e 