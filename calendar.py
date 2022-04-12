import calendar
#week_days = ["Sunday", "Monday", "Tuesday", "Wendnesday", "Thursday", "Friday", "Saturday"]
calendar.setfirstweekday(6)
date = input("Please specify a date: ('dd/mm/yyyy')")
dd = int(date[:2])
mm = int(date[3:5])
yyyy = int(date[6:])


cal_weekday = calendar.weekday(yyyy, mm, dd)


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