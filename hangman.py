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
    
# main program starts here
    
word_list = import_word_list()