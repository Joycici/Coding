#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 23: Read some code
This is not a script which can be run.
'''
"""
__author='Joycici'
__version__='1.0' 
"""

# github代码https://github.com/geekcomputers/Python/blob/master/sqlite_check.py

# Script Name	: sqlite_check.py
# Author		: Craig Richards
# Created		: 20 May 2013
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Runs checks to check my SQLITE database 
# 检查sqlite数据库

import sqlite3 as lite # 给库起别名
import sys
import os 

dropbox= os.getenv("dropbox")
dbfile=("Databases\jarvis.db")
master_db=os.path.join(dropbox, dbfile)
con = None

try:
    con = lite.connect(master_db) # 连接数据库
    cur = con.cursor()  #获得游标
    cur.execute('SELECT SQLITE_VERSION()') # 执行查询数据库版本
    data = cur.fetchone() # 获取单条数据
    print "SQLite version: %s" % data

# 如果try发现异常，则执行except内容
except lite.Error, e:

    print "Error %s:" % e.args[0]   # 输出error
    sys.exit(1) #退出
#不论如何finally都执行
finally:

    if con:
        con.close()  #关闭数据库连接

# 查询数据库所有表名
con = lite.connect(master_db)
cur=con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
rows = cur.fetchall() # 获得全部数据
for row in rows: #循环输出表名
  print row

# 与上一段查询内容一致
con = lite.connect(master_db)
cur=con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
while True:
  row = cur.fetchone()
  if row == None:
    break
  print row[0]