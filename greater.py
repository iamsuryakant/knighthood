# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:25:48 2019

@author: surya
"""
a=[]
for i in range (int(input("enter the number of elements"))):
    a.append(int(input("enter the number")))
for i in range (len (a)):
    min_fn=i
    for j in range (i+1,len(a)):
        if a[min_fn]>a[j]:
            min_fn=j
    a[i],a[min_fn]=a[min_fn],a[i]
print("the sorted array is: ")
for i in range (len(a)):
    print(a[i])
    