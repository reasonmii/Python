'''
cumsum
Creates a list of partial sums

- Use itertools.accumulate() to create the accumulated sum for each element
- Use list() to convert the result into a list

https://www.30secondsofcode.org/python/s/cumsum
'''

from itertools import accumulate

def cumsum(r):
  return list(accumulate(r))


# Example
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]


