# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:00:00 2021

@author: dipak
"""

"""
 Q_1
 Given a list of names, try printing unique names that are less than 5 
 character length and doesn't contain the character 'e'.
"""

names = ["john", "jake", "jack", "george", "jenny", "jason"]
for name in names:
    if len(name) < 5 and 'e' not in name:
        print(name)

print("\n")

"""
 Q_2
 Given a string python, try printing cython using slicing [start:stop] 
 and concatenation. +
"""

str = "python"
print('c' + str[1:])

print("\n")

"""
 Q_3
 Given a dictionary {"name": "python", "ext": "py", "creator": "guido"}, 
 print both keys and values.
"""

dict = {"name": "python", "ext": "py", "creator": "guido"}
print(f'Keys: {dict.keys()}')
print(f'Values: {dict.values()}')

print("\n")

for i in dict:
    print(f'Key: {i}, Value: {dict[i]}')

print("\n")

"""
 Q_4
 Fizz Buzz Program
 Write a Python program which iterates the integers from 1 to 50. For 
 multiples of three print "Fizz" instead of the number and for the multiples 
 of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
"""
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)


print("\n")

"""
 Q_5
 Guess number program using if else blocks
"""
number = 7

user_number = int(input("Guess our number!!! : "))
if user_number == number:
    print("You guessed correctly!")
elif abs(number - user_number) == 1:
    print("You were off by 1.")
elif user_number > number:
    print("Your number is greater than the actual number")
else:
    print("Your number is less than the actual number")