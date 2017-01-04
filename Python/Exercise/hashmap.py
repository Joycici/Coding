#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 39-2: hashmap.py
注释写的简直错乱...
'''
"""
__author='Joycici'
__version__='1.0' 
"""
# 初始化aMap，[]填充
def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([]) # 效果为[[],[],[]...]
    return aMap

# 将key的字符串转化为数字
def hash_key(aMap,key):
    """Given a key this will create a number and then convert it to an 
    index for the aMap's buckets."""
    return hash(key) % len(aMap) # hash 是python内置函数hash(object)
# 获取列表aMap[hash_key(..)]位置的值,例如 [('Michigan', 'MI')]，如果找不到返回[]
def get_bucket(aMap,key):
    """Given a key , find the bucket where it would go."""
    bucket_id = hash_key(aMap,key) #bucket_id即为hash_key计算出的hash值
    # print "follow1",bucket_id
    return aMap[bucket_id]  #通过hash值招到value，如 [('Michigan', 'MI')]
# 获取插槽位置，返回值的i,k，v分别为，关于i如果key存在从0开始返回，如果不存在返回-1,k,v是key value
# 如果没有招到key则返回-1，key,None 
def get_slot(aMap,key,default=None):
    """
    Return the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default(None if not set) when not found.
    """
	# aMap[bucket_id]返回值给bucket
    bucket = get_bucket(aMap,key)
    # print "follow",bucket
    # i是索引，kv是bucket内容
    for i, kv in enumerate(bucket): # 取0号位置及其值 bucket的内容赋给i,kv 
        # print "follow",kv
        k, v = kv #？kv的值怎么赋给k和v 1.bucket 中的内容是aMap的值即kv，它是一个key,value会被赋给等号左边的两个值
        # print "follow",k
        # print "follow",v
        if key == k:
            return i, k, v 

    return -1,key,default

def get(aMap,key,default=None):
    """Gets the value in a bucket for the given key,or the default."""
    i, k, v  =get_slot(aMap,key,default=default)
    print "get.print ",i,k,v
    return v 

def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    print "begin_set aMap:",aMap," key: ",key," value: ",value
    bucket = get_bucket(aMap,key)
    print "bucket = get_bucket: ", bucket
    i, k, v = get_slot(aMap, key)
    print "i,k,v = get_slot: ",i,k,v
    if i>=0:
        # the key exists, replace it
        bucket[i] = (key, value)
        print "update the value of the key :bucket[%d] " % i 
    else:
        # the key does not, append to create it
        bucket.append((key,value))
        print "after append ",bucket

def delete(aMap,key):
    """Delets the given key from the Map."""
    bucket = get_bucket(aMap, key)
    
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """Prints out what's in the Map"""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k,v 