
'''
months_diff
Calculates the month difference between two dates

- Subtract start from end and use datetime.timedelta.days to get the day difference
- Divide by 30 and use math.ceil() to get the difference in months (rounded up)

https://www.30secondsofcode.org/python/s/months-diff
'''

from datetime import date
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)

  
# Example
months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1

