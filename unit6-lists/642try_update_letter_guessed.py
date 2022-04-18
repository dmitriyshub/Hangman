def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """

    :param letter_guessed: The string represents the character received from the player
    :type letter_guessed: str == "letter"
    :param old_letters_guessed: The list contains the letters the player has guessed so far
    :type list of string
    :return:
    True if:
    If the character is correct (i.e. one English letter) and has not been guessed before, the function will add the character letter_gueesed to old_letters_guessed
    False if:
    """

    letter_guessed = letter_guessed.lower()
    old_letters_guessed =  list(map(str.lower, old_letters_guessed))

    if letter_guessed.isalpha() == True and len(letter_guessed) == 1 and letter_guessed not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed)
        return True

    elif letter_guessed.isalpha() == False or len(letter_guessed) > 1 or letter_guessed in old_letters_guessed:
        old_letters_guessed = sorted(old_letters_guessed)
        fail_string = ' -> '.join(old_letters_guessed)
        print("X\n",fail_string)
        return False


def main():
    print(try_update_letter_guessed("$",["b","c","a"]))

if __name__ == "__main__":
    main()