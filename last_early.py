def last_early(my_str):
    """
    This function gets string and returns True if there is the last letter in the string and False vice versa
    :param my_str: string to check
    :return: True if there a double letters or False
    """
    my_str = my_str.lower() # my_str to lower case
    n = len(my_str) # saves the length of my_str
    if len(my_str) == 1:
        # checks if the length of the string is 1 letter and returns False
        return False
    for i in range(1, n):
        # iterate for letters in my_str

        if my_str[-1] in my_str[0:-2]:
            # Checks if the last letter in my_str?
            return True
        else:
            return False




print(last_early("daXmxan"))