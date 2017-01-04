#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 33: While Loops
'''
"""
__author='Joycici'
__version__='1.0' 
"""

i = 0 
numbers = []

# while i < 6 :
    # print "At the top i is %d " %i 
    # numbers.append(i)

    # i = i + 1
    # print "Numbers now: ", numbers
    # print "At the bottom i is %d " % i 

# print "The numbers: "

# for num in numbers:
    # print num

# def number_append(i):
    # if i < 6:
        # numbers.append(i)
        # i = auto_incream(i,1)
        # number_append(i)

def auto_incream(i,step):
    return i + step

# number_append(i)


for i in range(6):
        numbers.append(i)
        i = auto_incream(i,1)   

		
print "The numbers: "

for num in numbers:
    print num