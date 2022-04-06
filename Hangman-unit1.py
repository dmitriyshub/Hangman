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
# number of attempts (randomly)
MAX_TRIES = 6

print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)

#the Hangman pictures

print("picture 1:")
print("x-------x")

print("picture 2:")
print("""x-------x
    |
    |
    |
    |
    |""")

print("picture 3:")
print("""x-------x
    |       |
    |       0
    |
    |
    |""")

print("picture 4:")
print("""x-------x
    |       |
    |       0
    |       |
    |
    |""")

print("picture 5:")
print("""x-------x
    |       |
    |       0
    |      /|\\
    |
    |""")

print("picture 6:")
print("""x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""")

print("picture 7:")
print("""x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")

