# the Hangman welcome page

HANGMAN_ASCII_ART = ("""
Welcome to the game Hangman \n
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

print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)

#gamer answer input
letter_answer = input("Guess a letter: ")
print("Your answer is: ", letter_answer)




