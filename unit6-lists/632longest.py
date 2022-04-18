def longest(my_list):
    """
    This function gets a list with strings and returns the longest string in the list
    :param my_list: list of strings
    :return: string
    """
    return max(my_list, key=len)

def main():
    print(longest(["111", "234", "2000", "goru", "birthday", "09"]))

if __name__ == "__main__":
    main()