#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 20:Functions and Files
'''
"""
__author='Joycici'
__version__='1.0' 
"""

from sys import argv

script, input_file = argv

# 用read()读取open(file)内容
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)
in_data = current_file.read()
a = len(in_data)
print a,type(a)


print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)
