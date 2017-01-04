#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 41:Learning To Speak Object Oriented
41代码要求保存文件名为oop_test.py
'''
"""
__author='Joycici'
__version__='1.0' 
"""
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# 字典PHRASES
PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
     "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":
     "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, and call it with parameters self,@@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) ==2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the websit
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    #随机的生成一个WORDS的副本列表，元素个数与%%%的个数相同
    #把这个列表的元素首字母大写并依次存放在class_names列表中
    class_names = [w.capitalize() for w in 
                   random.sample(WORDS, snippet.count("%%%"))] #snippet里面有几个%%%
    print "snippet.count: ",snippet.count("%%%")
    print "TEST class names: ",class_names
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
	
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase: #取key,取value 一共两个值
        result = sentence[:]
        print "sentence 为:",sentence, "      result为",result
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) #用随机选出的word替换%%%
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1) # 用随机选出的word替换***

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
	
        results.append(result) #将key和value的值拼接到一起
    print "Covert Results = ",results
    return results

# keep going until they hist Ctrl-C  
try:
    while True:
        snippets = PHRASES.keys() #获取PHRASES的key部分
        print "snippet: ", snippets 
        random.shuffle(snippets) #shuffle() 方法将序列的所有元素随机排序。
        
        for snippet in snippets: #从打乱顺序的序列中循环读出snippet
            phrase = PHRASES[snippet] # 获得value
            print "for snippet and phrase: ",snippet, phrase
            question, answer = convert(snippet, phrase) #将key,value传入convert
            if PHRASE_FIRST:
                question, answer = answer, question #调换参数内容
   
            print question
 
            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"			
	