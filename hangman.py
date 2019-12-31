# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:18:28 2019

@author: Sam
"""

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
    # code here
    return word_list[1]

# main program starts here
    
word_list = import_word_list()
selected_word = select_word(word_list)