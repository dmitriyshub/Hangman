
"""Choose from following options:

1: print your list
2: print how much items in your list
3: check if item in list
4: count the item in list
5: remove item from list
6: adding item to list
7:print all the wrong items
8: remove all duplicates from list
9: Exit

"""

def targil():

    user_string = input("Please input your shoping list (Items must be separated by ',' without spaces): ")
    user_list = user_string.split(',')
    count_goods = 0
    power = True

    while power == True:
        user_number = int(input("Please press a number from 1 - 9: "))
        answer3 = ""
        answer4 = ""
        answer5 = ""
        answer6 = ""

        if user_number == 1:
            print("Your list: ", user_list)

        elif user_number == 2:
            count_goods = len(user_list)
            print("Number of items in list: ", count_goods)

        elif user_number == 3:
            answer3 = input("Find item in list: ")

            if answer3 in user_list:
                print(True)
            else:
                print(False)

        elif user_number == 4:
            answer4 = input("Count specific item: ")
            print(user_list.count(answer4), "from this item in list!")

        elif user_number == 5:
            answer5 = input("remove specific element from list: ")
            print(answer5, "removed")
            user_list.remove(answer5)

        elif user_number == 6:
            answer6 = input("add item to your list: ")
            user_list.append(answer6)

        elif user_number == 7:
            invalid_list = []
            for i in user_list:
                condition = i.isalpha()
                element_length = len(i)
                if condition == False or element_length < 3:
                    invalid_list.append(i)
            print("invalid items in list: ")
            print(invalid_list)

        elif user_number == 8:
             user_list = set(user_list)
             print("Your new list:", user_list)


        elif user_number == 9:
            print("Goodbay!")
            power = False

def main():
    targil()

if __name__ == "__main__":
    main()






