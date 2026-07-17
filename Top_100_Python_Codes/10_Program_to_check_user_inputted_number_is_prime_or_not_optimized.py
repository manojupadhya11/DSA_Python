# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:48:16 2026

@author: Manu
"""

#10_Program_to_check_user_inputted_number_is_prime_or_not_optimized

def is_prime(num):
    flag = 1
    if num < 2:
        flag = 0
    for i in range(2, int(num ** 0.5)+1):
        if num%i == 0:
            flag = 0
            break
    
    
    return flag

num = int(input("Enter the value of num "))
print(is_prime(num))
if is_prime(num) == 0:
    print("not prime")
else:
    print("prime")