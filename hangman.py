# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:18:28 2019

@author: Sam
"""
from random import randint
# from string import ascii_lowercase

def import_word_list():
    """import word list from .txt file"""
    f = open('word_list.txt', 'r')
    word_list = f.readlines()
    f.close()
    return word_list

def select_word(word_list):
    """select a random word from the list"""
    n = randint(0,99)
    return word_list[3].strip()

# main program starts here

word_list = import_word_list()
word = select_word(word_list)
word_length = len(word)
word_unsolved = "*" * word_length
all_guesses = []
lives = 3

while True:
    # update word_unsolved
    word_unsolved = str()
    for i in range(word_length):
        if word[i] in all_guesses:
            word_unsolved = word_unsolved + word[i]
        else:
            word_unsolved = word_unsolved + "*"
    
    if word_unsolved == word:
        break
    
    if lives == 0:
        break
    
    print("You have %d lives remaining. The current word is: %s" % (lives, word_unsolved))
    guess = input("Please enter your next guess: ")
    # error check - exactly 1 character, letter a-z
    all_guesses.append(guess)
    
    if guess in word:
        print("Correct")
        
    else:
        print("Incorrect")
        lives -= 1

if word_unsolved == word:
    print("Congratulations you win")
    
elif lives == 0:
    print("You lose")
    
else:
    print("You broke the game!")    