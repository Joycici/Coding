#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 34: Accessing Elements of Lists
'''
"""
__author='Joycici'
__version__='1.0' 
"""


animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
sequence = ['first','second','third','fourth','fifth','sixth']
i = 0

for i in range(len(animals)):
    print "The first animal is at %d and is a %s " % (i, animals[i])
    print "The animal at %d is the %s animal and is a %s " % (i, sequence[i],animals[i])
	