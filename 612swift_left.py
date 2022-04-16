def shift_left(my_list):
    """
    This function gets list with 3 elements and returns new shifted list one step left
    :param: my_list: list of 3 elements - my_list[0, 1, 2]
    :type: my_list: list
    :return: new list shift one step left
    :rtype: list
    """
    new_list = []
    new_list.append(my_list.pop(1))
    new_list.append(my_list.pop(1))
    new_list.append(my_list.pop(0))

    return new_list



def main():
    print(shift_left([0, 1, 2]))
    print(shift_left(['monkey', 2.0, 1]))

if __name__ == "__main__":
    main()