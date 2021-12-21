'''
tail
Returns all elements in a list except for the first one

- Use slice notation to return the last element if the list's length is more than 1
- Otherwise, return the whole list

https://www.30secondsofcode.org/python/s/tail
'''

def tail(lst):
  return lst[1:] if len(lst) > 1 else lst


# Example
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]

