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
    return word_list[3].strip()

# main program starts here
    
word_list = import_word_list()
selected_word = select_word(word_list)
word_length = len(selected_word)

# python strings https://www.w3schools.com/python/python_strings.asp

# next: display letters as asterisks
# then: prompt for first guess

unsolved_word = "*" * word_length
all_guesses = []

for n in range(7):
    print("the current word is: ", unsolved_word)
    guess = input("Please enter your next guess: ")
    all_guesses.append(guess) 