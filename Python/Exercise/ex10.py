#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__author='Joycici'
__version__='1.0' 
"""
tabby_cat = "\tI'm tabbled in. "
persian_cat = "I'm split\non a line."
backslach_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
test_cat = """"""

print tabby_cat
print test_cat
print persian_cat
print backslach_cat
print tabby_cat
print fat_cat
print tabby_cat

# 结果表名"""会前后空行
#下面代码死循环打印一个*
# while True:
	# for i in ["/", "-", "|", "\\", "|"]:
		# print "%s\r" % i,
#???unicode不明白，下面部分为了表达什么？		
#a = "\' \" \a \b \f \n \N{96} \r \t \uxxxx \Uxxxxxxxx \v \ooo \xhh "
#print "\s" % a
#print "\r" % a

a = "a "
print "This is \s" % a
print "This is \r" % a