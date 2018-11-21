
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Student name: Matthew Dempster
# Student ID: 10388106
# Date: 2018-11-21
# Exam for B8IT105 Programming for Big Data
# Lecturer Darren Redmond
###############################################################################

import unittest
from Practice import Palindrome
# =============================================================================
# Test Palindrone
# =============================================================================

class Palindromes(unittest.TestCase):
    def SetUP(self):
        self.P = Palindrome()
        
    def test_palindrome(self):
       self.SetUP()
       self.assertEqual(True,self.P.isPalindrome("deed"))
       self.assertEqual(False,self.P.isPalindrome("Foobar"))
#    def test_palindromes(self):
#      
#        self.assertEqual(True, self.p.isPalindrome(self,'deed'))
if __name__ == '__main__':
    unittest.main()