
'''
every_nth
Returns every nth element in a list

- Use slice notation to create a new list
  that contains every nth element of the given list

https://www.30secondsofcode.org/python/s/every-nth
'''

def every_nth(lst, n):
  return lst[n-1::n]


# Example
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]

