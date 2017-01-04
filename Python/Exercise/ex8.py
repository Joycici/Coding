#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__author='Joycici'
__version__='1.0' 
"""

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)

print formatter % ("one", "two", "three", "four")

print formatter % (True, False,False,True)

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
	"I had this thing.",
	"That you could type up rith.",
	"But it didn't sing.",
	"So I said goodnight."
)

# 输出倒数第二行时为"，因为句子中存在did't 影响的
