#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
__author='Joycici'
__version__='1.0' 
"""
# 假设有汽车100辆
cars = 100
# 设每辆车空间能做4个人
space_in_a_car = 4.0
# 司机30人
drivers = 30
# 有乘客90人
passengers = 90
# 没有车的司机
cars_not_driven = cars - drivers
# 有多少量车被开
cars_driven = drivers
# 车的运输能力=被开周的车的
carpool_capacity = cars_driven * space_in_a_car
# 每辆车有多少乘客
average_passengers_per_car = passengers / cars_driven

print "There are", cars,"cars available."
print "There are only", drivers,"drivers available."
print "There will be ",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."


"""
Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined

"""
# 第八行，变量car_pool_capacity没有定义

# 附加题
# 1 不是必须得，本例中汽车空间不能按半个算；使用浮点数计算结果也会保留为浮点数，如果使用整型，计算结果也会是整型
# 2. 