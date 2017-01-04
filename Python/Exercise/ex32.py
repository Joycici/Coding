#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 32: Loops and List
'''
"""
__author='Joycici'
__version__='1.0' 
"""

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes',3, 'quarters']

# this first kind of for-loop goes through a list 
for fruit in fruits:
    print "A fruit of type: %s " % fruit


# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in items
for i in change:
    print "I got %r " % i

# we can also build lists, first start with an empty one

elements = []

# then use the range function to do 0 to 5 counts

for i in range(0, 6):
    print "Adding %d to the list ." %i 
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too 
for i in elements:
    print "Element was : %d " % i 

'''
1. Take a look at how you used range. Look up the range function to understand it.
返回一个整型数字列表，不包含stop值
2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?
Yes, for example. eg. t1 = (i for i in range(5))
3. Find the Python documentation on lists and read about them. What other operations can you do to lists besides append?
count() extend(iterable) index(value,[start,[stop]]) insert(index,object) pop([index]) remove(value) reverse() sort()
'''