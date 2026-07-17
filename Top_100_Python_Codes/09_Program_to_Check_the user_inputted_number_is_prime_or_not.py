# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:25:09 2026

@author: Manu
"""

#Program to check whether the user inputted number is prime or not
num1 = int(input("Enter the number to check prime or not "))
flag = 0
for i in range(2,num1):
    if num1%i == 0:
        flag = 1
        break

if flag == 1:
    print("Not prime number")
else:
    print("prime number")