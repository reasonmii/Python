
'''
take
Returns a list with n elements removed from the beginning

- Use slice notation to create a slice of the list
  with n elements taken from the beginning

https://www.30secondsofcode.org/python/s/take
'''

def take(lst, n):
    return lst[:n]


# Example
take([1, 2, 3], 5) # [1, 2, 3]
take([1, 2, 3], 0) # []
