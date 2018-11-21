
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Student name: Matthew Dempster
# Student ID: 10388106
# Date: 2018-11-21
# Exam for B8IT105 Programming for Big Data
# Lecturer Darren Redmond
###############################################################################

"""
Created on Tue Nov 20 22:26:56 2018

@author: Administrator
"""

# a)	Create a class in Python called Calculator.
#
# In your Calculator class, implement methods called triple(), third(),
# fourth_order(), and fourth_order_root() which take a list of numbers as an
# argument and return the appropriate result.
#
# These should be implemented with the map and lambda functions.
#
# For example, if the argument is [1, 2, 3] for the triple() function it will
# return [3, 6, 9].

class Calculator(object):

    def __init__(self):
        self.variable = 0

    def triple(self, x):
        return list(map(lambda x: x*3, x))

    def third_order_root(self, x):
        return list(map(lambda x: x*1/3, x))

    # fourth order means x^4 and fourth order root means x^1/4
    def fourth_order(self, x):
        return list(map(lambda x: x*4, x))

    def fourth_order_root(self, x):
        return list(map(lambda x: x*1/4, x))
    
calc =   Calculator()
print(calc.triple([1,2,3]))

calc =   Calculator()
print(calc.third_order_root([3, 6, 9]))


calc =   Calculator()
print(calc.fourth_order([1,2,3]))

calc =   Calculator()
print(calc.fourth_order_root([4, 8, 12]))


# [6 marks]
#
# b)	Evaluate the Big‐O classification for the following functions.
# i.	f(n) = 4*n ‐ 1
# ii.	f(n) = 6*log n – 2
# iii.	f(n) = 2*n^4 + 9*n^3 + 5
# iv.	f(n) = 6*n^2 + (1+9*n)*3n^2
# v.	f(n) = 5*n + 8*n
# vi.	f(n) = 21
# [6 marks]

# Take highest term, drop multiplier, and drop all lower order terms

# i.	f(n) = 4*n ‐ 1                         O(n)
# ii.	f(n) = 6*log n – 2                     O(log(n))
# iii.	f(n) = 2*n^4 + 9*n^3 + 5               O(n^4)
# iv.	f(n) = 6*n^2 + (1+9*n)*3n^2            O(n^3)
# v.	f(n) = 5*n + 8*n                       O(n)
# vi.	f(n) = 21                              O(1)

#i.     f(n) = 4*n ‐ 1 
#       = 4n -1
#       =0(n)

#ii     f(n) = 6*log n – 2 
#       =6logn-2
#       =0(log(n))
#
#iii    f(n) = 2*n^4 + 9*n^3 + 5 
#       2n^4 + 9n^3 + 5 ##drop number before n put 0 and remove + or minus
#       0n4 +0n^3
#       0(n^4)
#
#iv     f(n) = 6*n^2 + (1+9*n)*3n^2 
#       6n^2 + 27n^3
#       n^2 +n^3
#       0(n^3)
#
#v      f(n) = 5*n + 8*n 
#       0(n)
#
# vi     f(n) = 21 
#       0(1)




# c)	Write a program to make a “Guess the Letter” game.
#
# The computer will think of a random letter from ‘a’ to ‘z’, and ask you to
# guess it. The computer will tell you if each guess is too high or too low in
# the alphabet. You win if you can guess the number within six tries.
# [13 marks]
#
# (Total: 25 Marks)

#correctLetter = "J"
#
#def check_guess (letter):
#
#    tries = 3
#
#    while tries > 0:
#
#        guess = input ("Enter your guess ")
#
#        if letter == guess.upper():                
#            print ("Correct!")
#            break
#
#        elif letter < guess.upper():
#            if tries > 1:
#                print ("You are wrong, but go closer to A")
#            tries = tries - 1    #Moves you closer to finishing the loop
#
#        elif letter > guess.upper():
#            if tries > 1:
#                print ("You are wrong, but go closer to Z")  
#            tries = tries - 1  #Moves you closer to finishing the loop
#
#    if tries == 0:
#        print ("GAME OVER!")
#
#check_guess(correctLetter)