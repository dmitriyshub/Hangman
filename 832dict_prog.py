my_dict = {'first_name': 'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act'] }

def dict_func():
    answer = int(input("Please choice a number between 1-7: "))
    if answer == 1:
        print(my_dict['last_name'])
    elif answer == 2:
        print(my_dict['birth_date'])
    elif answer == 3:
        print(len(my_dict['hobbies']))
    elif answer == 4:
        print(my_dict['hobbies'][2])
    elif answer == 5:
        my_dict['hobbies'].append('Cooking')
    elif answer == 6:
        my_dict['birth_date'] = tuple(map(int, my_dict['birth_date'].split('.')))
        print(my_dict['birth_date'])
    elif answer == 7:
        my_dict['Age'] = '52'
        print(my_dict['Age'])
    else:
        print("You doing something wrong!")

dict_func()