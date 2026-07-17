# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:15:58 2026

@author: Manu
"""

#Program to check whether the user inputted year is leap year or not 

year = int(input("Enter a year "))

if ((year%4 == 0 and year%100!=0) or year%400 == 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")