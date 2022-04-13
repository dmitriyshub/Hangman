def last_early(my_str):
    my_str = my_str.lower()
    n = len(my_str)
    if len(my_str) == 1:
        return False
    for i in range(1, n):

        if my_str[-1] in my_str[0:-2]:
            return True
        else:
            return False




print(last_early("H"))