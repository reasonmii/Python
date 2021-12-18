'''
1) from_iso_date
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


'''
2) to_iso_date
Converts a date to its ISO-8601 representation

- Use datetime.datetime.isoformat() to convert the given datetime.datetime object
  to an ISO-8601 date

https://www.30secondsofcode.org/python/s/to-iso-date
'''

from datetime import datetime

def to_iso_date(dt):
    return datetime.isoformat(dt)


# Example
to_iso_date(datetime(2020, 10, 25)) # 2020-10-25T00:00:00

