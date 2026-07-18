# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 05:23:06 2026

@author: Manu
"""

#program to calculate Find the sum of the Digits of a Number in Python

num = int(input("Enter a Number"))
sum = 0
for i in range (1, num+1):
    x = int(num%10)
    sum = sum+x
    num = num//10
    
    
print(sum)



