# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:58:50 2019

@author: surya
"""
class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if age<13:
            print("you are young")
        elif age>=13 and age<18:
            print("You are a teenager")
        else:
            print("You are old")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        global age
        age+=1

        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
