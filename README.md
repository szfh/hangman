# Hangman

## Plan

1. Import list of words from ``word_list.txt`` :tick:
1. Select random word from list :tick:
1. Display letters as asterisks ``*******``
1. Prompt for guess
	1. Correct: display letter with asterisks filled ``**a**a*``
	1. Incorrect: remove life and display asterisks ``*******``
1. Continue until
	1. Win: word complete
	1. Lose: 7 incorrect guesses

## Task

### A project for the jHub Coding Scheme (JCS)

There are four easy steps to complete the assessment.

**Step 1**: First up you need to create an Idea - just click the ``Add idea`` button below and title it with your service number, initials, the module and challenge number (i.e. ``34340011-JK_Mod3_Chal1``)

**Step 2**: Once you have created your idea - attach a completed "Plagiarism declaration" disclaimer (template attached in right-side taskbar) that all of the work uploaded to the site is your own, and also attach your certificate of course completion/a screenshot to prove you personally completed the module if Udacity (not providing this means half payment - this is because it wouldn't be fair for those who already have the skills to receive the same amount of money as those who had to learn it from scratch).

**Step 3**: Your assignment is to code, in python 3, a game of hangman. Specifically the program should choose a word from a predefined bank of words (the attached ``word_list.docx`` - you should download this and convert it to a .txt file, unfortunately .txt files cannot be attached to this site, frustratingly), and display to the user how many letters the word is (i.e. ``*******``. The user should then be able to guess one letter at a time, with the program either taking a "life" from them if it is an incorrect guess, or showing that the letter is correct and where it appears in the word (i.e. ``***a**a*``). The game ends when the user runs out of guesses (let's say 7 incorrect guesses) or the player has filled in all the letters of the word.

We require that the program you write does some things in a very specific way so please follow the bullet points below to the letter otherwise your program will be automatically failed.

* The program must run in Python3 without error. :snake:
* The script must ONLY stop to either ask for the next guess or because the game has been won or lost (i.e. no menus or other user input).
* Asking the user to make her next guess must use the following text (case sensitive and a space after the colon are necessary (I think)): ``Please enter your next guess: ``
* The text printed before ``Please enter your next guess: `` must END in the word to be guessed with the unknown letters starred out (i.e. hello would start as ``*****`` and change into ``*e***`` after ``e`` was guessed). The string must not contain any other stars.
* The program must print either ``congratulations you win`` or ``you lose`` on exit (not case sensitive).
* When a game is played, a word must be picked randomly (from a uniform distribution) from the ``word_list.txt`` file.
* The ``word_list.txt`` file must be stored in the same path as your code and when you load the file don't include the path (i.e. ``open('word_list.txt', ...)``).
* If the user makes 7 wrong guesses then they lose the game.

Emailing code to us is no longer acceptable due to MoDNET restrictions, and this site doesn't allow python file upload. Instead, the code should be saved on this website: https://gist.github.com (you will have to create a free account), with the naming convention ``Surname_FirstName_Hangman.py`` as a ``Secret gist`` and then the link pasted into your ``Idea`` submission on this page. The mark-scheme is attached on the right-side of this page, and we expect completion of the project to take around 10-20 hours. The solution can easily found on google - PLEASE try to figure it out on your own - we run plagiarism checkers :wink:

**Step 4** : Once completed, we will trawl the submissions once a month (first fortnight of the month), mark them, and get back to you with whether you have passed.