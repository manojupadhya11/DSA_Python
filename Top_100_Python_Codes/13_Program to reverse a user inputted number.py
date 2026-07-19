# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 05:31:29 2026

@author: Manu
"""

#Program to reverse a user inputted number


num1 = int(input("Enter a number  "))
num2 = 0

while num1 > 0:
    rem = int(num1%10)
    num2 = int(num2*10+rem)
    num1 = num1//10

    
    
print(num2)