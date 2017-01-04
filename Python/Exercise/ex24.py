#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 24: More Practise
This is not a script which can be run.
'''
"""
__author='Joycici'
__version__='1.0' 
"""

print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The loveloy world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requeires an explanation
\n\t\twhere there is none.

"""

print "-------------------"
print poem
print "-------------------"

five = 10 - 2 + 3 - 6
print "This should be five : %s " % five 

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10 

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates. " % secret_formula(start_point)