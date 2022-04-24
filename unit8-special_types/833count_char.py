def count_chars(my_str):
    """
    This function count the letters of my_str in dictionary
    :param my_str: str
    :return: dict
    """
    count_dict = {}
    for letter in my_str:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    if ' ' in count_dict:
        del count_dict[' ']
    return count_dict


magic_str = "abra cadabra"
print(count_chars(magic_str))