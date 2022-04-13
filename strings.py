# replace letters in the string:

""" first:
answer = input("Please enter a string:")
first_letter = answer[0]
rest_sentence = answer[1:].replace("d", "e")
final_answer = first_letter + rest_sentence
print(final_answer)
"""
""" second: (final answer)
fix_me = input("Enter a string: ")
first_letter = fix_me[0]
print(first_letter + fix_me[1:].replace(first_letter, 'e'))
"""

# input a string and get an output with the string that contains first lower case chars and the other half with upper case
user_string = input("Please enter your string: ")
print(int(len(user_string)) // 2)
first = user_string[0:4]
second = user_string[4:]
first = first.lower()
second = second.upper()
print(first + second)
