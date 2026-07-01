# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 22:36:49 2026

@author: Manu
"""

#Pyhton program 05
#Program to calulate sum of natural number in range

range1 = int(input("Enter lower range "))
range2 = int(input("Enter higher range "))
sum=0
for i in range(range1,range2+1):
    sum = sum+i

print(sum)