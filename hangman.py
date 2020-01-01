# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:18:28 2019

@author: Sam
"""
from random import randint
from string import ascii_lowercase

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
    # update word_unsolved
    word_unsolved = str()
    for i in range(word_length):
        if word[i] in all_guesses:
            word_unsolved = word_unsolved + word[i]
        else:
            word_unsolved = word_unsolved + "*"

    print("You have %d lives remaining. The current word is: %s" % (lives, word_unsolved))
    guess = input("Please enter your next guess: ")
    # error check - exactly 1 character, letter a-z
    all_guesses.append(guess)
    
    if guess in word:
        print("Correct")
        
    else:
        print("Incorrect")
        lives -= 1
    
    # victory
    
    # death
    
    # #for l in word_length
    # #if selected_word[l] in guess
    # #unsolved_word[l] = guess
    
# test
# test_lives = 3
# test_all_guesses = ["a","b","c"]
# # test_not_guessed = ascii_lowercase - test_all_guesses
# test_word = "sugar"
# test_word_unsolved = "*" * 5

# for l in range(5):
#     print("letter = %s" %test_word[l])
#     if test_word[l] == "a":
#         print("l = %d" %l)
    