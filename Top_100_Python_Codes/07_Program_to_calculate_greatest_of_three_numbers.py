# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:01:51 2026

@author: Manu
"""

#Program to calculate greatest of three numbers in the given user inputted value

num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))
num3 = int(input("Enter number 3 "))


if num1 >= num2  and num1 >= num3:
    print(num1,"is greater than ",num2, "and",num3)
elif num2 >= num1 and num2 >= num3:
    print(num2,"is the greater than ",num1,"and",num3)
elif num3 >= num1 and num3 >= num2:
    print(num3,"is the greater than ",num1,"and",num2)

