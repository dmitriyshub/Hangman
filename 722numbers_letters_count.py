def numbers_letters_count(my_str):
    new_list = []
    number_count = 0
    string_count = ""
    for i in my_str:
        if i.isdigit():
            number_count = number_count + int(1)
        else:
            string_count += i

    new_list.append(number_count)
    new_list.append(len(string_count))
    return new_list


def main():
    print(numbers_letters_count("Python 3.6.3"))


if __name__ == "__main__":
    main()