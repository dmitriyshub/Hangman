def seven_boom(end_number):
    """

    :param end_number: number
    :return: if there a number 7 or the number divided by 7 replace i for string "BOOM"
    """
    boom_list =[]
    for i in range(end_number+1):
        if i % 7 == 0:
            boom_list.append('BOOM')
        elif '7' in str(i):
            boom_list.append('BOOM')
        else:
            boom_list.append(i)
    return boom_list

def main():
    print(seven_boom(30))

if __name__ == "__main__":
    main()