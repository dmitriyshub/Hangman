course_dict = {'I': 3, 'love': 3, 'self.py!': 2}

def inverse_dict(my_dict):
    """
    This function reverse dict values and keys
    :param my_dict: dict
    :return: new dict
    """
    new_dict = {}
    index = 0
    dict_keys = list(my_dict.keys())
    dict_values = list(my_dict.values())
    for value in dict_values:
        if value not in new_dict:
            new_dict[value] = []
    for value in dict_values:
        new_dict[value].append(dict_keys[index])
        new_dict[value].sort()
        index += 1

    return new_dict

print(inverse_dict(course_dict))