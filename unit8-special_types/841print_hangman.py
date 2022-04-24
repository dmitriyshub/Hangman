HANGMAN_PHOTOS = {
        1: 'x-------x',

        2: 'x-------x\n'
           '|\n'
           '|\n'
           '|\n'
           '|\n'
           '|\n',

        3: 'x-------x\n'
           '|       |\n'
           '|       0\n'
           '|\n'
           '|\n'
           '|\n',

        4: 'x-------x\n'
           '|       |\n'
           '|       0\n'
           '|       |\n'
           '|\n'
           '|\n',

        5: 'x-------x\n'
           '|       |\n'
           '|       0\n'
           '|      /|\\\n'
           '|\n'
           '|\n',

        6: 'x-------x\n'
           '|       |\n'
           '|       0\n'
           '|      /|\\\n'
           '|      /\n'
           '|\n',

        7: 'x-------x\n'
           '|       |\n'
           '|       0\n'
           '|      /|\\\n'
           '|      / \\\n'
           '|\n',

}


def print_hangman(num_of_tries):

    return print(HANGMAN_PHOTOS[num_of_tries])

def main():
    print_hangman(num_of_tries=6)

if __name__ == "__main__":
    main()