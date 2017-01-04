#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 19: Function and Variable
'''
"""
__author='Joycici'
__version__='1.0' 
"""
# 定义函数，输出cheese_count, boxes_of_crackers
def Cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

# 直接输入数字作为入参
print "We can just give the function numbers directly:"
Cheese_and_crackers(20,30)

# 输入变量作为入参
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

Cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# 输入数学计算作为入参
print "We can even do math inside too:"
Cheese_and_crackers(10 + 20, 5 + 6)

# 输入变量+数字的数学计算作为入参
print "And we can combine the two, variables and math:"
Cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 通过raw_input输入变量
print "Input cheeses: "
c1 = raw_input('cheese number> ')
print "Input crackers: "
c2 = raw_input('crackers nuber> ')

Cheese_and_crackers(int(c1),int(c2))


