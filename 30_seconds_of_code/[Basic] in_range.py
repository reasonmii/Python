
'''
in_range
Checks if the given number falls within the given range

- Use arithmetic comparison to check if the given number is in the specified range
- If the second parameter, end, is not specified, the range is considered to be from 0 to start

https://www.30secondsofcode.org/python/s/in-range
'''

def in_range(num, start, end=0):
    return start <= num <= end if end >= start else end <= num <= start


# Example
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
