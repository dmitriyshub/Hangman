import calendar

#week_days = ["Sunday", "Monday", "Tuesday", "Wendnesday", "Thursday", "Friday", "Saturday"] (Can make an implamantation of this function with list later)

calendar.setfirstweekday(6) # the default first number in the calendar function is Monday[0] and the last is Sunday[6]
date = input("Please specify a date: ('dd/mm/yyyy')") # input from user with Date

dd = int(date[:2]) # slicing of Days
mm = int(date[3:5]) # slicing of Months
yyyy = int(date[6:]) # slicing od Years


cal_weekday = calendar.weekday(yyyy, mm, dd) # weekday method of cal function is check for day number of the week

# Conditions for day weeks
if cal_weekday == 6:
    print('Sunday')
elif cal_weekday == 0:
    print('Monday')
elif cal_weekday == 1:
    print('Tuesday')
elif cal_weekday == 2:
    print('Wednesday')
elif cal_weekday == 3:
    print('Thursday')
elif cal_weekday == 4:
    print('Friday')
else:
    print('Saturday')