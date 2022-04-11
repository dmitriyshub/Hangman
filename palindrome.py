# final solution
str = input(str("enter your words: "))
str_low = str.lower()
str_no_spaces = str_low.replace(" ", "")
str2 = str_no_spaces[-1::-1]
if str_no_spaces == str2:
    print("OK")
else:
    print("NO")

# not correct solution
"""
if str[:] == str[::-1]:
    answer = 'OK'
else:
    answer = 'NOT'
print(answer)
"""