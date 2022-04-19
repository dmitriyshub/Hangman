def show_hidden_word(secret_word, old_letters_guessed):
    """

    :param secret_word: The string represents the secret word the player needs to guess
    :param old_letters_guessed: A list contains the letters the player has guessed so far
    :return:
    """
    secret_word_len = len(secret_word)
    game_desk = ("_" * secret_word_len)
    temp_list = list(game_desk)
    counter = 0
    for i in secret_word:

        if i in old_letters_guessed:
            temp_list[counter] = ' ' + i
            counter += 1
        elif i not in old_letters_guessed:
            temp_list[counter] = ' _'
            counter += 1
    game_desk = "".join(temp_list)
    game_desk = game_desk[1:]
    return game_desk


def main():
    print(show_hidden_word('banana', ['c','b','a']))

if __name__ == "__main__":
    main()