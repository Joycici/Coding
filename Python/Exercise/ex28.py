#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 28: Boolean Practice
This practice should be running on python shell, so there is no coding on this
Or, we can use print to show results.
'''
"""
__author='Joycici'
__version__='1.0' 
"""

print "The result should be True, isn't it? Type the result: %r" % (True and True)
print "The result should be False, isn't it? Type the result: %r" % (False and True)
print "The result should be False, isn't it? Type the result: %r" % (1 == 1 and 2 == 1)
print "The result should be True, isn't it? Type the result: %r" % ("test" == "test")
print "The result should be True, isn't it? Type the result: %r" % (1 == 1 and 2 != 1)
print "The result should be True, isn't it? Type the result: %r" % (True and 1 == 1)
print "The result should be False, isn't it? Type the result: %r" % (False and 0 != 0)
print "The result should be True, isn't it? Type the result: %r" % (True or 1 == 1)
print "The result should be False, isn't it? Type the result: %r" % ("test" == "testing")
print "The result should be False, isn't it? Type the result: %r" % (1 != 0 and 2 == 1)
print "The result should be True, isn't it? Type the result: %r" % ("test" != "testing")
print "The result should be False, isn't it? Type the result: %r" % ("test" == 1)
print "The result should be True, isn't it? Type the result: %r" % (not (True and False))
print "The result should be False, isn't it? Type the result: %r" % (not (1 == 1 and 0 != 1))
print "The result should be False, isn't it? Type the result: %r" % (not (10 == 1 or 1000 == 1000))
print "The result should be True, isn't it? Type the result: %r" % (not ("testing" == "testing" and "Zed" == "Cool Guy"))
print "The result should be True, isn't it? Type the result: %r" % (1 == 1 and (not ("testing" == 1 or 1 == 0)))
print "The result should be False, isn't it? Type the result: %r" % ("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print "The result should be False, isn't it? Type the result: %r" % (3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))


# 附加题
'''
== 等于!= 不等于>= 大于等于 <= 小于等于
 
'''
'''
python和很多语言可以返回布尔表达式中的一个操作数，而不仅仅是真或假。
这意味着如果你计算False and 1 你会得到表达式的第一个操作数 (False) ，
但是如果你计算True and 1的时候，你得到它的第二个操作数(1)。试一试吧。
'''
print "test" and "test"  #返回test
print "test" and 1 #返回1
print 1 and "test" #返回test
print True and 1 # 1
print 1 and True # true
print False and 1 # false
print 1 and False # false
print 0 and True # 0
print True and 0 #0
print 0 and False #0 
print False and 0 #false ???为什么不是0？
print 1 or False  # 返回1
print 0 or False  # false