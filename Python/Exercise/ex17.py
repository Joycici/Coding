#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 17:More File
'''
"""
__author='Joycici'
__version__='1.0' 
"""
from sys import argv
from os.path import exists

scripte, from_file, to_file = argv

print  "Copying from %s to %s" % (from_file,to_file)

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# print "This input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_input()

out_file = open(to_file,'w')
out_file.write(indata)



print "Alright, all done."

in_file.close()
out_file.close()

# 写成一行
#open(to_file,'w').write(open(from_file).read())

# 为什么要close python会自动释放文件，但是有一些情况不自动释放，从编码规范上讲，应该手动close

# 