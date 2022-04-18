# the final answer
def filter_teens(a = 13, b = 13, c = 13):
    """

    :param a: children 1 age
    :param b: children 2 age
    :param c: children 3 age
    :return:
    """
    return fix_age(a) + fix_age(b) + fix_age(c)


def fix_age(age):
    if (age >=13) and (age <= 19) and (age != 15) and (age != 16):
        age = 0
        return age
    else:
        return age


"""another 
sum = 0
def filter_teens(a = 13,b = 13,c = 13):
    age_list = [a,b,c]
    new_age_list = []
    for i in age_list:

    if(a or b or c >=13 <= 19 and (a or b or c != 15 or 16)) :
        for i in age_list:
            new_age_list.append(fix_age(i))
        else:
            new_age_list.append(i)
        return new_age_list


print(filter_teens(2,13,1))



Final_Result = filter_teens()
print(Final_Result)
"""

