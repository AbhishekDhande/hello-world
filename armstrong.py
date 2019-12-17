# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:01:50 2019

@author: abhis
"""

num = int(input("Please Enter any number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
   
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")