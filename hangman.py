# -*- coding: utf-8 -*-
"""
@author: Samuel
"""
from random import randrange

# functions
def select_word():
    """import word_list.txt, then return a random word"""
    f = open("./word_list.txt", "r") # read in all words from file
    word_list = f.readlines()
    f.close()
    
    n = randrange(len(word_list)) # select a random word
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
    if not len(guess) == 1: # invalid if more or less than 1 character
        print("enter 1 character")
        return False
    elif not guess.islower(): # invalid if not lower case character
        print("enter a lower case character")
        return False
    elif guess in all_guesses: # invalid if alredy guessed
        print("you've tried that one already")
        return False
    else:
        all_guesses.append(guess) # valid if none of above conditions matched
        return True

def win(word, word_unsolved):
    """check if the game has been won"""
    if word_unsolved == word:
        return True
    else:
        return False

def lose(lives):
    """check if the game has been lost"""
    if lives == 0:
        return True
    else:
        return False

def life_lives(lives):
    """give the singular or plural version of life/lives"""
    if lives == 1:
        return "life"
    else:
        return "lives"

# main program
word = select_word() # get word for puzzle
word_length = len(word) # get word length
all_guesses = [] # empty list of guesses
lives = 7 # starting number of lives

while True:
    word_unsolved = game(word, all_guesses)
    if win(word, word_unsolved): # end game if all letters guessed
        break
    
    if lose(lives): # end game if all lives lost
        break
    
    # print game status
    print("You have %d %s remaining. The current word is: %s" %(lives, life_lives(lives), word_unsolved))
    
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

if  win(word, word_unsolved): # end game
    print("Congratulations you win")
elif lose(lives):
    print("You lose")
else:
    print("You broke the game!")    