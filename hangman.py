# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:18:28 2019

@author: Sam
"""
from random import randint

def import_word_list():
    """import word list from .txt file"""
    print("Importing word list")
    # code here
    f = open('word_list.txt', 'r')
    word_list = f.readlines()
    f.close()
    print("Import complete")
    return word_list

def select_word(word_list):
    """select a random word from the list"""
    n = randint(0,99)
    return word_list[n].strip()

# main program starts here
    
word_list = import_word_list()
selected_word = select_word(word_list)
word_length = len(selected_word)
print(selected_word)

#python strings https://www.w3schools.com/python/python_strings.asp