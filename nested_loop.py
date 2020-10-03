# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:46:10 2020

@author: lukin
"""
#Циклами while
print('_____________________________________')
print('Циклами while: ')
i = 0
j = 0
k = '\U0001f600'
while i < 10:
    while j < i:
        k += '\U0001f600'
        j += 1
    print(k)
    i += 1
    
#Циклами for - while
print('_____________________________________')
print('Циклами for - while: ')
for number in range(10):
    count = 0
    smile = ''
    while count <= number:
        smile += '\U0001f600'
        count += 1
    print(smile)
    
#Циклами for
print('_____________________________________')
print('Циклами for: ')
for number in range(10):
    smile = ''
    for count in range(number + 1):
        smile += '\U0001f600'
    print(smile)
    
#String animation
print('_____________________________________')
print('String animation: ')
for number in range(1, 11):
    print('\U0001f600' * number)

#List Comprehension
print('_____________________________________')
print('List Comprehension: ')
a = [print('\U0001f600' * num) for num in range(1, 11)]