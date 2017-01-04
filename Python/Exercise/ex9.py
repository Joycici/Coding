#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__author='Joycici'
__version__='1.0' 
"""

# Here's some new strange studff,remember type it exactly.

days = "Mon Tue Web Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nJun\nJul\nAug"

print "Here are the days: " , days
print "Here are the months: " , months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
# 发现错误 由于print 打成pirnt，但是报错在第16行，报的是无效字符，其实是认为print后面是一行？
#
#PS E:\python\Exercise> python .\ex9.py
#  File ".\ex9.py", line 16
#    """
#      ^
#SyntaxError: invalid syntax
#"""

# 第二次报错，因为试图用"""进行跨行注释，但是中间包含^ 直接报错了
#PS E:\python\Exercise> python .\ex9.py
#  File ".\ex9.py", line 22
#    ^
#    ^
#IndentationError: unexpected indent


""" 
abc
bcd
"""

