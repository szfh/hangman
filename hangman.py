# -*- coding: utf-8 -*-
"""
@author: Samuel
"""
from random import randint

def select_word():
    """import word_list.txt, then return a random word"""
    f = open("./word_list.txt", "r") # read in all words from file
    word_list = f.readlines()
    f.close()
    
    n = randint(0,len(word_list)-1) # select a random word
    word = word_list[n].strip() # remove white space
    return word

def game(word, all_guesses):
    """get the current game status"""
    word_unsolved = str() # empty string
    for i in range(word_length): # loop through each letter in word
        if word[i] in all_guesses:
            word_unsolved = word_unsolved + word[i] # enter letter if guessed
        else:
            word_unsolved = word_unsolved + "*" # enter * if not guessed
    return word_unsolved

def check_guess_valid(guess, all_guesses):
    """check that a guess is valid"""
    if not len(guess) == 1: # invalid if more than 1 character
        print("enter 1 letter")
        return False
    elif not guess.islower(): # invalid if not lower case character
        print("enter a lower case letter")
        return False
    elif guess in all_guesses: # invalid if alredy guessed
        print("you've tried that one already")
        return False
    else:
        all_guesses.append(guess) # valid if none of above conditions matched
        return True

# main program starts here
word = select_word() # get word for puzzle
word_length = len(word) # get word length
all_guesses = [] # empty list of guesses
lives = 7 # starting number of lives

while True:
    word_unsolved = game(word, all_guesses)
    if word_unsolved == word: # end game if all letters guessed
        break
    
    if lives == 0: # end game if all lives lost
        break
    
    # print game status
    print("You have %d lives remaining. The current word is: %s" %(lives, word_unsolved))
    
    while True:
        guess = input("Please enter your next guess: ") # get next guess
        if check_guess_valid(guess, all_guesses): # break while loop if guess is valid
            break
        else: # continue until a valid guess is entered
            continue
    
    if guess in word: # check if guess is correct
        print("Correct")
        
    else:
        print("Incorrect")
        lives -= 1 # lose a life if guess is incorrect

if word_unsolved == word: # end game
    print("Congratulations you win")
elif lives == 0:
    print("You lose")
else:
    print("You broke the game!")    