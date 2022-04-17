def squared_numbers(start, stop):
    """
    This function gets 2 numbers and save all the squared value in the list e.g 2,4 --> [4,6,8]
    :param start: start number
    :type int or float
    :param stop: stop number
    :type int or float
    :return: list of numbers
    """
    squared_list = []
    while start <= stop:
        squared_number = start * start
        squared_list.append(squared_number)
        start += 1

    return squared_list

def main():
    print(squared_numbers(-3,3))

if __name__ == "__main__":
    main()

