#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 31:Making Decisions
P2 附加题
'''
"""
__author='Joycici'
__version__='1.0' 
"""

print "Please guess a number, I will give you some info to make you near it."

your_number = int(raw_input("> "))

my_number = 49

if your_number < 0 :
    print "You can't input negative number!"
elif your_number > 100:
    print "Your number can't be greater than 100!"
else:
    print "Your number is between 0 and 100 , it's Ok!"
    if your_number > my_number:
        print "You should input a smaller one."
    elif your_number < my_number:
        print "You should input a bigger one."
    else:
        print "Great job!."

