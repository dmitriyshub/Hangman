def check_win(secret_word, old_letters_guessed):
    word_len = len(secret_word)
    correct_answer = 0
    for i in secret_word:
        if i in old_letters_guessed:
            correct_answer += 1
    if word_len == correct_answer:
        return True
    else:
        return False




def main():
    print(check_win('banana', ['n', 'b', 'z']))

if __name__ == "__main__":
    main()