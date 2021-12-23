'''
1) drop
Returns a list with n elements removed from the left

- Use slice notation to remove the specified number of elements from the left
- Omit the last argument, n, to use a default value of 1

https://www.30secondsofcode.org/python/s/drop
'''

def drop(lst, n=1):
  return lst[n:]


# Example
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []


'''
2) drop_right
Returns a list with n elements removed from the right

- Use slice notation to remove the specified number of elements from the right
- Omit the last argument, n, to use a default value of 1

https://www.30secondsofcode.org/python/s/drop-right
'''

def drop_right(lst, n=1):
  return lst[:-n]


# Example
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
