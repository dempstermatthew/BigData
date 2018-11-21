
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Student name: Matthew Dempster
# Student ID: 10388106
# Date: 2018-11-21
# Exam for B8IT105 Programming for Big Data
# Lecturer Darren Redmond
###############################################################################
"""
Created on Tue Nov 20 22:09:04 2018

@author: Administrator
"""

import unittest

from Question_3_10388106 import DocumentAnalyser


class Q3_checker(unittest.TestCase):

    def setUp(self):
        file_name =  'C:\\Users\\Administrator\\Downloads\\simplefile.txt'
        self.class_test = DocumentAnalyser(file_name)

    def test_DocumentAnalyser(self):
        self.assertEqual(2, self.class_test.number_lines_file())
        # This should include test for each method
        self.assertEqual(8, self.class_test.number_of_words())
        self.assertEqual(35, self.class_test.number_of_character())
        self.assertEqual(17.5, self.class_test.av_no_of_chars_per_line())
        self.assertEqual(4, self.class_test.av_no_of_words_per_line())
        self.assertEqual(4.375, self.class_test.av_no_of_chars_per_word())


if __name__ == '__main__':
    unittest.main()