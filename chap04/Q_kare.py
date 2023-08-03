import calendar


def colored_calendar(year, month):
    cal = calendar.month(year, month)
    colored_cal = cal.replace("Sa", "\033[91mSa\033[0m")
    colored_cal = colored_cal.replace("Su", "\033[91mSu\033[0m")
    return colored_cal


print(colored_calendar(2023, 8))
print(type(colored_calendar(2023, 8)))
