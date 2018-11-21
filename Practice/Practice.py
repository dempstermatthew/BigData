
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

class BankAccount(object):
    interest_rate = 0.3
    
    def __init__(self, name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance

## name the class variables and the instance variables int he code
        #class varaible is interest_rate and instance variables are  name, number, balance
        
    def deposit(self,amount):
        self.balance += amount
    
    def withdrawl(self,amount):
        if amount < self.balance :
            self.balance -= amount
    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        
class StudentAcccount(BankAccount):
    
    def _init__(self, name, number,balance):
        BankAccount.__init__(self, name, number,balance)
        self.overdraft = 1000
    def withdrawl(self, amount):
        if amount < self.balance + self.overdraft :
            self.balance -= amount
            
            
class Palindrome(object):
    pass
    def reverse(self,value):
        return value[::-1]
    
    def isPalindrome(self, value):
        return value == self.reverse(value)
if __name__ == '__main__':
    p = Palindrome()
    print(p)
    print(p.reverse('Foobar'))
    print(p.isPalindrome('deed'))
    print(p.isPalindrome('Foobar'))
    def sum_list(seq):
         return sum(seq)
    a=[1,2,2,2]
    print(sum_list(a))