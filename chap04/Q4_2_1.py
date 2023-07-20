def number_to_day(num=0):
    if num == 0:
        day = "wednesday"
    elif num == 1:
        day = "thursday"
    elif num == -1:
        day = "tuesday"
    elif num == -2:
        day = "monday"
    elif num == 2:
        day = "friday"
    elif num == 3:
        day = "saturday"
    elif num == -3:
        day = "sunday"
    else:
        day = "trueday"
    return day


day = number_to_day(3)
print(day)
