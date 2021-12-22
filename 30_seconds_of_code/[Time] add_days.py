
'''
add_days
Calculates the date of n days from the given date

- Use datetime.timedelta and the + operator
  to calculate the new datetime.datetime value after adding n days to d
- Omit the second argument, d, to use a default value of datetime.today()

https://www.30secondsofcode.org/python/s/add-days
'''

from datetime import datetime, timedelta, date

def add_days(n, d = datetime.today()):
    return d + timedelta(n)


# Example
add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)

