# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:47:15 2019

@author: surya
"""

def insertionSort(a):
    for i in range (1,len(a)):
        key=a[i]
        j=i-1
        while j >= 0 and key < a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
a=[12,0,9,4,13,15]
insertionSort(a)
print("sorted array is:")
for i in range (len(a)):
    print(a[i])