#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 40: Modules,Classes,and Objects
'''
"""
__author='Joycici'
__version__='1.0' 
"""

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]
)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
						
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


a = "la la lala lalala"
b = ["la la lala lalala","aaa aaa aaa"]
lll = Song(a) # 当a为一个字符串的时候，for line in a表示输出其中每一个字母
lll.sing_me_a_song()
lll1 = Song(b) # 加大括号将其变为一个完整的列表
lll1.sing_me_a_song()