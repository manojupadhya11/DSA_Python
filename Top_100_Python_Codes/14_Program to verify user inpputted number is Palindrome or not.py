# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 05:45:56 2026

@author: Manu
"""

#Palindrome Number

num1 = int(input("Enter a number  "))
num2 = 0
temp = num1
while num1 > 0:
    rem = int(num1%10)
    num2 = int(num2*10+rem)
    num1 = num1//10

    
    
if num2  == temp:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
    
    