def format_list(my_list):
    """
    This function gets list of even number strings len(my_list) == 2 or == 4 or == 6 and so on ...
    :param my_list: ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    :return: list of string with onlu the even strings in my_list >> hydrogen, lithium, boron, and magnesium
    """
    comma = ", "
    str_to_end = ", and "
    last_word = my_list[-1]
    my_new_list = comma.join(my_list[::2])  + str_to_end + last_word
    return my_new_list

def main():
    print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

if __name__ == "__main__":
    main()


"""def format_list(my_list):
    This function gets list of even number strings len(my_list) == 2 or == 4 or == 6 and so on ...
    :param my_list: ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    :return: list of string with onlu the even strings in my_list >> hydrogen, lithium, boron, and magnesium
    
    comma = ", "
    str_to_end = "and "
    last_word = my_list[-1]
    my_new_list = comma.join(my_list[::2])  + str_to_end + last_word
    return my_new_list

def main():
    print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

if __name__ == "__main__":
    main()"""