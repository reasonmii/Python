
'''
days_diff
Calculates the day difference between two dates

- Subtract start from end
  and use datetime.timedelta.days to get the day difference

https://www.30secondsofcode.org/python/s/days-diff
'''

from datetime import date

def days_diff(start, end):
    return (end - start).days


# Example
days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3

