# the final answer:
def distance(num1, num2, num3):
    """
    This function gets 3 numbers
    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    return ((abs(num1 - num2) == 1) or (abs(num1 - num3) == 1)) and (((abs(num2 - num3) > 1) and (abs(num2 - num1) > 1)) or ((abs(num3 - num2) > 1) and (abs(num3 - num1) > 1)))





print(distance(1,2,10))

"""another:  
a = abs(num1)
b = abs(num2)
c = abs(num3)
closed_absolute = 1
print(a,b,c)
if [(abs(num2-num1)) == 1 or (abs(num3-num1) == 1)] and [(abs(num2 - num1) > 1) and (abs(num3 - num2) > 1) or (abs(num3 - num1) > 1) and(abs(num3 - num2) > 1)]:
    return True
else:
    return False"""
