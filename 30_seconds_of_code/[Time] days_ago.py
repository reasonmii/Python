
'''
days_ago
Calculates the date of n days ago from today

- Use datetime.date.today() to get the current day.
- Use datetime.timedelta to subtract n days from today's date.

https://www.30secondsofcode.org/python/s/days-ago
'''

from datetime import date, timedelta

def days_ago(n):
    return date.today() - timedelta(n)


# Example
days_ago(5) # datetime.date(2021, 12, 15)


# reference =====================================================

timedelta(5)
# datetime.timedelta(days=5)
