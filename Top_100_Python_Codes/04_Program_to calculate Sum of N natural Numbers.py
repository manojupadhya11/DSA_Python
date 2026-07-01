# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 22:31:22 2026

@author: Manu
"""

#Python Program 04  Using Recursion
#Program to calculate sum of n Natural Numbers in recursion method

def recur_sum(num):
    if num ==0:
        return num
    return num + recur_sum(num-1)

num = int(input("enter a number "))
sum = 0

print("Sum of Natural Number is",recur_sum(num))