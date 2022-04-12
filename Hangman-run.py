# the Hangman welcome page

HANGMAN_ASCII_ART = ("""
  Welcome to the Hangman Game! \n
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/  \n


 """)
#max number of attempts
MAX_TRIES = 6

print(HANGMAN_ASCII_ART, "Max tries: ", MAX_TRIES)

#gamer answer input
letter_answer = input("  Guess a letter please: ")
letter_answer = letter_answer.lower()
print("  Your answer is: ", letter_answer)

if letter_answer.isalpha() == False and len(letter_answer) > 1:
    print("E3")
elif letter_answer.isalpha() == False:
    print("E2")
elif len(letter_answer) > 1:
    print("E1")
else:
    print("your doing something wrong")

#building a game table
word_answer = input("Please enter a word:  ")

word_len =len(word_answer)
print("_ " * word_len)

