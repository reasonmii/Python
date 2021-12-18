
'''
from_iso_date
Converts a date from its ISO-8601 representation

- Use datetime.datetime.fromisoformat() to convert
  the given ISO-8601 date to a datetime.datetime object

https://www.30secondsofcode.org/python/s/from-iso-date
'''

from datetime import datetime

def from_iso_date(dt):
    return datetime.fromisoformat(dt)
    

# Example
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
