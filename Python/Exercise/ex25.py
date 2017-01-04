#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 25: Even more Practise
This is not a script which can be run.
'''
"""
__author='Joycici'
__version__='1.0' 
"""
'''
import os
#获取当前工作目录
>>>os.getcwd()
#更改当前工作目录
>>>os.chdir('d:\')
>>>os.getcwd()
可以import当前目录下的.py文件
import a
or
from a import * 
'''

# 空格拆分
def break_words(stuff):
    """This function will break up words for us.""" #这个可以通过help(ex25)获取到
    words = stuff.split(' ')
    return words
# 单词排序
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
# 删除并取第一个单词
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
# 删除并取最后一个单词
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
# 调用break_words返回切分后的单词并排序
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
# 切分后打印第一个单词和最后一个
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
# 切分排序后，删除并打印第一和最后一个单词
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

