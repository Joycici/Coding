#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
统计happiness_seg.txt 中，出现频率最高的前 10 个「二元词组」，并输出它们的频率。
「二元词组」即文章中所有接连出现的两个词，如「今天 天气 不错」有「今天 天气」，「天气 不错」两个「二元词组」
"""

__author__ = 'Joycici'
__version__ = '1.0'

import  re
from collections import Counter
import langid
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def is_chinese(uchar):
    """通过langid包判断是否是汉字"""
    return langid.classify(uchar)[0] == 'zh'
def print_mullist(list):
    """将双层list结果输出到屏幕，比如[[a,b],[b,c]]"""
    for i in list:
        for j in i:
            print j
def main():
    # 读入数据
    with open('E:\TestingData\happiness_seg.txt','r+') as happiness_seg_file:
        seg_word = happiness_seg_file.read().split(" ")

    # 组成二元词组
    phrase_list = []
    for i in range(0,len(seg_word)-1):
        if is_chinese(seg_word[i]) and len(seg_word[i])==6:
            if is_chinese(seg_word[i+1]) and len(seg_word[i+1])==6:
                phrase_list.append(" ".join((seg_word[i],seg_word[i+1])))

    # 统计出现次数
    num = Counter(phrase_list)
    top_10_word =  num.most_common(10)
    # 测试输出前十个
    print_mullist(top_10_word)
    # 关闭文件
    happiness_seg_file.close()

if __name__ == '__main__':
    main()

