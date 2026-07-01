# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 22:20:30 2026

@author: Manu
"""

#Python Program 02
#02 Program to check whether the user inserted Number is even or ODD

num = int(input("Enter a Number "))

if num<0:
    print("Enter a Positive Number")
    num = int(input("Enter a Number "))
elif num%2==0:
    print(f"{num} is Even Number")
else:
    print(f"{num} is Odd Number")