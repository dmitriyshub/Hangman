def is_valid_input(letter_guessed):
    """
    This function checks if the input is valid
    :param letter_guessed: string of one letter
    :type letter_guessed: str
    :return: (False/True, letter_guessed)
    :rtype: (bool, str)
    a. False if letter_guessed string is two or more letters
    b. False if letter_guessed contains a special symbol (*,& ...)
    c. True if the str is contain letter in english
    """

    if letter_guessed.isalpha() == False and len(letter_guessed) > 1:
        return False
    elif letter_guessed.isalpha() == False:
        return False
    elif len(letter_guessed) > 1:
        return False
    elif letter_guessed.isalpha() == True and len(letter_guessed) == 1:
        return True

def main():
    print(is_valid_input("a"))

if __name__ == "__main__":
    main()