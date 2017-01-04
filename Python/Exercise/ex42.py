#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Exercise 42: Is-A，Has-A，Objects，and Classes
'''
"""
__author='Joycici'
__version__='1.0' 
"""

## Animal is-a object (yes, sort of confusing ) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name 

## Cat is-a animal
class Cat(Animal):
   
    def __init__(self, name):
        ## Cat has-a name  
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
    ## person has-a name 
    self.name = name 

    ## Person has-a pet of some kind
    self.pet = None



## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a  Fish 

class Salmon(Fish):
    pass

## Halibut is a Fish .
class Halibut(Fish):
    pass
	

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is a person 
mary = Person("Mary")

## mary has-a pet 
mary.pet = satan

## frank has-a name and salary
frank = Employee("Franck", 12000)

## frank has-a pet 
frank.pet = rover

## a Fish instance named flipper
flipper = Fish()

## a Salmon instance named crouse
crouse = Salmon()

## a Halibut instance named harry
harry = Halibut()

