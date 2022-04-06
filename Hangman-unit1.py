import random
#the Hangman welcome page
print("Welcome to the game Hangman")
print(""" 
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
 
 
 """)
# number of attempts (randomly)
randomNumber = random.randint(5, 10)
print(randomNumber)


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

