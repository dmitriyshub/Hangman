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

