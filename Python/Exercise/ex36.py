#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 36 :Designing and Debugging
'''
"""
__author='Joycici'
__version__='1.0' 
"""

'''

做什么：
判断生活精彩程度，判断标准：
下班后是出门还是回家
     出门得一分，回家为0分
周末是出门还是回家
     出门的一分，回家不得分
回家后看小说打游戏和家人一起
		看书1 打游戏-3 家人+4

		
统计得分 2分以上 good 负分 bad 0分Normal

可以无限次重做，除非输入放弃

'''
from sys import exit

def night_where(core):
    "下班后是出门还是回家"
    print "You should choice 'go home ' or 'go out'"
    choice = raw_input("> ")
	
	
    if choice == "go home":
        core += 0
        core = what_did_you_do(core)
    elif choice == "go out":
        core += 1
    else:
        dead("Error")
    return core		
	
def weekday_where(core):
    "周末是出门还是回家: 出门的一分，回家不得分"
    print "You should choice 'go home ' or 'go out'"
    choice = raw_input("> ")
	
	
    if choice == "go home":
        core += 0
        core = what_did_you_do(core)
    elif choice == "go out":
        core += 1
    else:
        dead("Error")
    return core

	
def what_did_you_do(core):
    "在家做什么"
    print "You should choice 'reading ' or 'play game ' or 'family'"
    choice = raw_input("> ")
	
	
    if choice == "reading":
        core += 1
    elif choice == "play game":
        core -= 3
    elif choice == "family":
        core += 4
    else:
        dead("Error")
    return core		

def which_class(core):
    "判断类别"
    if core == 0:
        print "Normal"
    elif core > 0 :
        print "Good"
    else :
        print "Bad"


def dead(err):
    print "Stop because %s" % err	


def start():
    
    while True:
        core = 0
        print "Begin!"
        core = night_where(core)
        core = weekday_where(core)
        print "core is %d" % core
        which_class(core)
        print "Do you want to stop? (Yes or No)"
        do_what = raw_input("> ")
        if do_what == "Yes":
            exit(0)
        else:
            print "Continue"
    

 

start()


	

