
'''
1) is_weekday
Checks if the given date is a weekday

- Use datetime.datetime.weekday() to get the day of the week as an integer
- Check if the day of the week is less than or equal to 4
- Omit the argument, d, to use a default value of datetime.today()

https://www.30secondsofcode.org/python/s/is-weekday
'''

from datetime import datetime, date

def is_weekday(d = datetime.today()):
    return d.weekday() <= 4


# Example
is_weekday(date(2020, 10, 25)) # False
is_weekday(date(2020, 10, 28)) # True


'''
2) is_weekend
Checks if the given date is a weekend

- Use datetime.datetime.weekday() to get the day of the week as an integer
- Check if the day of the week is greater than 4
- Omit the second argument, d, to use a default value of datetime.today()

https://www.30secondsofcode.org/python/s/is-weekend
'''

from datetime import datetime, date

def is_weekend(d = datetime.today()):
    return d.weekday() > 4


# Example
is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False


# reference =====================================================

date(2021, 12, 24).weekday()  # 4 -> Friday
date(2021, 12, 26).weekday()  # 6 -> Sunday
date(2021, 12, 27).weekday()  # 0 -> Monday
