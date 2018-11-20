#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Student name: INSERT NAME HERE
# Student ID: INSERT ID HERE
# Date: 2018-11-21
# Exam for B8IT105 Programming for Big Data
# Lecturer Darren Redmond
###############################################################################

import unittest

from Q4 import ClassName


class Q3_checker(unittest.TestCase):

    def setUp(self):
        ''' This runs at the start, create objects to test here '''
        self.class_test = ClassName()

    def test_DocumentAnalyser(self):
        ''' Actual tests '''
        self.assertEqual(0, self.class_test.method1())
        self.assertEqual(0, self.class_test.method2())


if __name__ == '__main__':
    unittest.main()
