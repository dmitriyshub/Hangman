def is_greater(my_list, n):
    """
    This function gets list of number and n number and returns new_list with all numbers greater than n
    :param my_list: list of numbers
    :param n: number
    :return: list of numbers
    """
    new_list = []
    for i in my_list:
        if i > n:
            new_list.append(i)
    return new_list


def main():
    print(is_greater([1, 30, 25, 60, 27, 28], 28))
if __name__ == "__main__":
    main()