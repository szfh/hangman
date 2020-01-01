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
word = select_word(word_list)
word_length = len(word)

# python strings https://www.w3schools.com/python/python_strings.asp

# next: display letters as asterisks
# then: prompt for first guess

word_unsolved = "*" * word_length
all_guesses = []

lives = 3
while lives > 0:
    print("You have %d lives remaining. The current word is: %s" % (lives, word_unsolved))
    guess = input("Please enter your next guess: ")
    # error check
    all_guesses.append(guess)
    
    if guess in word:
        print("Correct")
        # update word_unsolved
        # breakpoint()
        l=0
        # for l in word_length:
            # breakpoint()
            # if word[l] in guess:
                # breakpoint()
                # word_unsolved[l] = guess
        
    else:
        print("Incorrect")
        # take away a life
    
    
    
    #for l in word_length
    #if selected_word[l] in guess
    #unsolved_word[l] = guess
    
    
    lives -= 1 # only if incorrect guess