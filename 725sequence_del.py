def sequence_del(my_str):
    """

    :param my_str: string
    :return: string without duplicates letters
    """
    current_letter = ""
    new_string = ""
    for letter in my_str:
        if letter != current_letter:
            new_string += letter
            current_letter = letter
    return new_string



def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))

if __name__ == "__main__":
    main()