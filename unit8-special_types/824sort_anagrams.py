
def sort_anagrams(list_of_strings):
    anagrams = []
    for string1 in list_of_strings:
        in_anagrams = []
        print(string1)
        for string2 in list_of_strings:
            print(string2)
            if sorted(string1) == sorted(string2):
                in_anagrams.append(string2)
        if in_anagrams not  in anagrams:
            anagrams.append(in_anagrams)





    return anagrams












list_of_words = ['apple', 'aplpe', 'dog']
print(sort_anagrams(list_of_words))

