# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:49:57 2021

@author: dipak
"""

"""
T_1
Improvise the guessing game from yesterday by providing 3 tries to the player
"""
from random import randint
guessesTaken = 0
myName = input('What is your name?\n')
number = randint(1, 20)
print('Hello, ' + myName + ', I am thinking of a number between 1 and 20')
while guessesTaken < 4:
    guess = int(input('Take a guess\n'))
    guessesTaken = guessesTaken + 1 
    if guess < number:
        print('Guess is too low. Try again')
    elif guess == number:
        break
    else:
        print('Guess is too high. Try again')
    

if guess == number:
    print('\nGood job, ' + myName + '! You guessed the correct number in ' +
          str(guessesTaken) + ' guesses!')

if guess != number:
    print('\noops. You have reached the guessing limit. The number that I was '
          +
          'thinking is ' + str(number))
    
"""
T_2
Given a list ['a', 'b', ...] print elements along with their position like 
0: a, 1: b one per line
"""
char_list = ['a','b','c','d','e','f']
for pos,char in enumerate(char_list):
    print(f"{pos}: {char}\n")

"""
T_3
Loop over a dict and print the value and key in the format value belongs to key.
"""
a_dict={'me': 'money', 'her': 'home', 'both': 'dog'}
for Key,Value in a_dict.items():
    print(f"{Value} belongs to {Key}\n")

"""
T_4
Demonstrate the else clause being invoked in a while loop. try the opposite as well.
"""
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

n = 5
while n > 0:
    n -= 1
    print(n)
    break
else:
    print('Loop done.')

"""
T_5
write an add function that accepts two numbers and returns their sum 
use type hints
use docstring
"""
def add(num1: int, num2: int) -> int:

    '''
    
    Returns the sum.
    
    Parameters:
        num1 (int): first number.
        num2 (int): second number.
    
    Returns:
        sum of two numbers.
    '''

    sum = num1 + num2
    return sum
    
print(add(4, 1))
print(add.__doc__)
help(add)

"""
T_6
write a function that accepts any number of args and prints them to the screen
 one per line
"""
def get_args(*args):
    for arg in args:
        print(f"\n {arg}")

get_args("luffy", "Zoro", "Nami","Brook", "God D. Usopp","jenny")
 
"""
T_7
write a function that accepts any number of kwargs and prints the number of 
args
"""

def get_Kargs(**kwargs):
    len_k = len(kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print(f"number of kwargs: {len_k} ")

get_Kargs(name= "test",language="py",creator="dooby")

"""
T_8
write a function that accepts any number of args and/or kwargs and prints 
the count of both
"""
def get_args_Kargs(*args,**kwargs):
    len_a = len(kwargs) + len(args)
    for arg in args:
        print(f"{arg}")
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print(f"count: {len_a} ")

get_args_Kargs("luffy", "Zoro", name= "test",language="py")

"""
T_9
Go through PEP 8, and try refactoring your code
"""
"""
T_10
Go through PEP 20 and let me know your fav one!
"""

"""
T_11
Do a while loop with and without else block getting invoked
"""

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

n = 5
while n > 0:
    n -= 1
    print(n)
    break
else:
    print('Loop done.')


"""
T_12
Do list comprehension to get odd numbers' squares from this list: 
    [1, 3, 3, 4, 5, 6]
"""
num_list=[1, 3, 3, 4, 5, 6]
new_list = [x** 2 for x in num_list if x%2 != 0]
print(new_list)

"""
T_13
write a lambda expression to return average given a total and count
"""
total=int(input("Enter the total : "))
count=int(input("Enter the count : "))
avg = lambda total, count : total /count
print(f"Average : {avg(total,count)}")

"""
T_14
Try list comp to get keys that are longer than 4 chars in a dict
"""
kvalues={'name':'test','language':'py','creator':'Tim','color':'red'}
ans = {k for k in kvalues.keys() if len(k) >4 }
print(ans)

"""
T_15
implement nested list comp in any use case
"""
fruits = [['apples','oranges'], ['bananas','mangoes'],['grapes','strawberry']] 
  
big_fruits = [fruit
                   for sublist in fruits
                   for fruit in sublist 
                   if len(fruit) > 6]           
print(big_fruits) 