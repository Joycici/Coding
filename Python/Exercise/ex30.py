#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 30: Else and If
'''
"""
__author='Joycici'
__version__='1.0' 
"""
# people = 30
# cars = 40
# trucks = 15
people = 30
cars = 20
trucks = 45

# 判断cars与people数量，做出不同行为，大于，小于，等于三种
if cars > people :
    print "We should take the cars."
elif cars < people :
    print "We should not take the cars."
else :
    print "We can't decide."

if trucks > cars:
    print "That's too many rucks."
elif trucks < cars :
    print "Maybe we could take the trucks."
else :
    print "We still can't decide."
# 如果people 大于 trucks ,执行A，小于等于执行B
if people > trucks :
    print "Alright,let's just take the trucks."
else:
    print "Fine, let's stay home then."
