def check_valid_input(letter_guessed, old_letters_guessed):
    """

    :param letter_guessed: the value of  input number from the user
    :param old_letters_guessed: list of all guessed letters
    :return: bool True or False
    False if:
    a. if string letter_guessed contain more than one letter
    b. if string letter_guessed contain special numbers
    c. if string letter_guessed letter already inside old_letters_guessed list
    True if:
    a. if string letter_guessed consists of one letter only and is not on the old_letters_guessed list
    """
    letter_guessed = letter_guessed.lower()
    old_letters_guessed =  list(map(str.lower, old_letters_guessed))
    if letter_guessed.isalpha() == False and len(letter_guessed) > 1 and letter_guessed in old_letters_guessed:
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    elif letter_guessed.isalpha() == False:
        return False
    elif len(letter_guessed) > 1:
        return False
    elif letter_guessed.isalpha() == True and len(letter_guessed) == 1 and letter_guessed not in old_letters_guessed:
        return True

def main():
    print(check_valid_input("f", ["d", "c", "a"]))

if __name__ == "__main__":
    main()