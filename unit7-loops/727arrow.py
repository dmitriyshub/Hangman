def arrow(my_char, max_length):
    """
    This function gets char and max length and prints arrow
    :param my_char: the char
    :param max_length: number
    :type max_length: int
    :return:
    """
    final_arrow = ''
    counter = 1
    if max_length == 1:
        return my_char
    for num in range(max_length):
        final_arrow += (my_char * counter)
        final_arrow += "\n"
        counter += 1
    counter -= 2
    for num in range(max_length - 1):
        final_arrow += (my_char * counter)
        final_arrow += "\n"
        counter -= 1
    return final_arrow[:-1]




def main():
    print(arrow('*', 10))

if __name__ == "__main__":
    main()


"""    
    
    for i in range(max_length + max_length):
        size = i
        if i >= max_length:
            size = max_length + max_length - i
        for j in range(size + size):
            if j < size:
                print(my_char, end='')
            else:
                print(my_char, end='')
        print()
"""

"""for i in range(max_length * 2):
    print_char = my_char
    if i <= 5:
        print(print_char * i)
    elif i > 5:
        print(print_char * (10 - i))
return"""