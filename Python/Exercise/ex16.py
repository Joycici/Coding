#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 16:Reading and writing Files
'''
"""
__author='Joycici'
__version__='1.0' 
"""
from sys import argv

script,filename = argv

# 输出待操作文件名字，判断是否要进行下一步的删除操作
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")
# 打开文件，并给予写权限
print "Opening the file..."
target = open(filename,'w')
# 删除文件内容
print "Truncating the file . Goodbye!"
target.truncate()
# 通过交互界面输入3行信息
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3：")

# 将刚刚输入的内容写入文件，每次换行
print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# 做题犯错记录，如果使用%r显示结果为'aaa'回车'bbb'，需要用%s,如果\n%s不连续，会出现空格
line  = "%s \n%s \n%s \n" % (line1,line2,line3)
target.write(line)

# 关闭文件
print "And finally, we close it."
target.close()

'''
p4 默认open() 是只读权限，如果不加 open(a,'w')不能修改文件
'''
