
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Student name: Matthew Dempster
# Student ID: 10388106
# Date: 2018-11-21
# Exam for B8IT105 Programming for Big Data
# Lecturer Darren Redmond
###############################################################################

#Create a class called DocumentAnalyser.
#number of lines in a file 
#number of words in a file 
#number of characters in a file 
#average number of characters per line in a file 
#average number of words per line in a file 
#average number of characters per word in a file  
class DocumentAnalyser(object):

    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_file(self.filename)
        self.__cnt_no_of_lines = 0
        self.__cnt_no_of_words = 0
        self.__cnt_no_of_characters = 0
    
    def read_file (self, myfilename):
        myfile = open(myfilename, 'r') 
        data = myfile.readlines()
        myfile.close()
        return(data)
                
    def number_lines_file (self):
        self.__cnt_no_of_lines = 0
        for line in self.data:
            self.__cnt_no_of_lines += 1
        return self.__cnt_no_of_lines
    
    def number_of_words(self):
        self.__cnt_no_of_words = 0
        for line in self.data:
            words = line.split()
            self.__cnt_no_of_words += len(words)
        return self.__cnt_no_of_words
    
    def number_of_character(self):
        self.__cnt_no_of_characters = 0
        for line in self.data:
            self.__cnt_no_of_characters += len(line)
        return self.__cnt_no_of_characters
    
    def av_no_of_chars_per_line (self):
        return self.__cnt_no_of_characters / self.__cnt_no_of_lines
    
    def av_no_of_words_per_line (self):
        return self.__cnt_no_of_words / self.__cnt_no_of_lines
    
    def av_no_of_chars_per_word (self):
        return self.__cnt_no_of_characters / self.__cnt_no_of_words

# Code under here will only run when we run this file.
# This stops it running when the test file is run


if __name__ == '__main__':
    filename = 'C:\\Users\\Administrator\\Downloads\\simplefile.txt'
    documentAnalyser = DocumentAnalyser(filename)
    print(documentAnalyser.data)
    print(documentAnalyser.number_lines_file())
    print(documentAnalyser.number_of_words())
    print(documentAnalyser.number_of_character())
    print(documentAnalyser.av_no_of_chars_per_line())
    print(documentAnalyser.av_no_of_words_per_line())
    print(documentAnalyser.av_no_of_chars_per_word())
