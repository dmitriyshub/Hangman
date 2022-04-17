fix_me = input("Enter a string: ")
first_letter = fix_me[0]
print(first_letter + fix_me[1:].replace(first_letter, 'e'))