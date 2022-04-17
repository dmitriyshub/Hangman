def are_lists_equal(list1, list2):
    """
    This function gets two lists with only int and float numbers and
    :param list1: list
    :param list2: list
    :return: True if both lists contain exactly the same numbers (even if in a different order) otherwise returns False
    """
    list1 = sorted(list1)
    list2 = sorted((list2))
    if list1 == list2:
        return True
    else:
        return False

def main():
    print(are_lists_equal([0.6, 1, 2, 3], [3, 2, 0.6, 1]))
    print(are_lists_equal([0.6, 1, 2, 3], [9, 0, 5, 10.5]))
if __name__ == "__main__":
    main()