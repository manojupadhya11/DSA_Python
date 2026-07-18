# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 05:07:17 2026

@author: Manu
"""

#Python Program to Print Prime Numbers In a Given Range

low = int(input("Enter a a number for low value "))
high = int(input("Enter a a number for high value "))


primes = []


for num in range(low, high+1):
    flag = 0
    
    if num < 2:
        continue    
    if num == 2:
        primes.append(2)
        continue
    
    for x in range (2, num):
        if num%x == 0:
            flag = 1
            break
        
        
    if flag == 0:
        primes.append(num)


print(primes)    