#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__author='Joycici'
__version__='1.0' 
"""
# name = 'Zed A. Shaw'
# age = 35 #not a lie 
# height = 74 # inches
# weight = 180 #lbs
# eyes = 'Blue'
# teeth = 'White'
# hair = 'Brown'

# print "Let's talk about %s." % name
# print "He's %d inches tall." % height
# print "He's %d pounds heavy." % weight
# print "Actually that's not too heavy."
# print "He's got %s eyes and %s hair." %(eyes,hair)
# print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
# print "If I add %d, %d, and %d I get %d." % (age, height, weight,age + height + weight)

name = 'Zed A. Shaw'
age = 35 #not a lie 
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight,age + height + weight)

# 英寸转化为厘米
my_height_centimeters = height * 2.54
my_weith_kilograms = weight * 0.4532

print "He's height is %r centimeters" % my_height_centimeters

print "He's height is %d centimeters" % my_height_centimeters
print "He's height is %r kilograms" % my_weith_kilograms
print "He's height is %d kilograms" % my_weith_kilograms