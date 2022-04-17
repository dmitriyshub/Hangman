letter_answer = input("  Guess a letter please: ")
letter_answer = letter_answer.lower()
print("  Your answer is: ", letter_answer)

if letter_answer.isalpha() == False and len(letter_answer) > 1:
    print("E3")
elif letter_answer.isalpha() == False:
    print("E2")
elif len(letter_answer) > 1:
    print("E1")
else:
    print("your doing something wrong")