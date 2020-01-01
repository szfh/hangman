# -*- coding: utf-8 -*-
"""
@author: Samuel
"""
from random import randint

def select_word():
    """import word_list.txt, then return a random word"""
    f = open('word_list.txt', 'r')
    word_list = f.readlines()
    f.close()
    
    n = randint(0,99)
    word = word_list[n].strip()
    return word

def game(word, all_guesses):
    """get the current game status"""
    word_unsolved = str()
    for i in range(word_length):
        if word[i] in all_guesses:
            word_unsolved = word_unsolved + word[i]
        else:
            word_unsolved = word_unsolved + "*"
    return word_unsolved

def check_guess_valid(guess, all_guesses):
    """check that a guess is valid"""
    if not len(guess) == 1:
        print("enter 1 letter")
        return False
    elif not guess.islower():
        print("enter a lower case letter")
        return False
    elif guess in all_guesses:
        print("you've tried that one already")
        return False
    else:
        all_guesses.append(guess)
        return True

# main program starts here
word = select_word()
word_length = len(word)
all_guesses = []
lives = 7

while True:
    word_unsolved = game(word, all_guesses)
    if word_unsolved == word:
        break
    
    if lives == 0:
        break
    
    print("You have %d lives remaining. The current word is: %s" %(lives, word_unsolved))
    
    while True:
        guess = input("Please enter your next guess: ")
        if check_guess_valid(guess, all_guesses):
            break
        else:
            continue
    
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