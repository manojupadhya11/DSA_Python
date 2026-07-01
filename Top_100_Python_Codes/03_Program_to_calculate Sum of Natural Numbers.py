# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 22:24:08 2026

@author: Manu
"""

#Python program 3
#Program to calculate sum of first n Natural Numbers

num = int(input("Enter a Number "))


sum = 0

for i in range(0,num+1):
    sum +=i
    
print(f"Sum of first {num} Natural Number is {sum}")

#Using Formula to calculate 

sum2 = int((num*(num+1))/2)
print(sum2)