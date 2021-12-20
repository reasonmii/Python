
'''
days_from_now
Calculates the date of n days from today

- Use datetime.date.today() to get the current day
- Use datetime.timedelta to add n days from today's date

https://www.30secondsofcode.org/python/s/days-from-now
'''

from datetime import date, timedelta

def days_from_now(n):
    return date.today() + timedelta(n)


# Example
days_from_now(5) # datetime.date(2021, 12, 25)
