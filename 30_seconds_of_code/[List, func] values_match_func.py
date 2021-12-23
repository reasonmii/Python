
'''
1) every
Checks if the provided function returns True for every element in the list

- Use all() in combination with map() and fn to check
  if fn returns True for all elements in the list

https://www.30secondsofcode.org/python/s/every
'''

def every(lst, fn = lambda x: x):
    return all(map(fn, lst))


# Example
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True


'''
2) some
Checks if the provided function returns True for at least one element in the list

- Use any() in combination with map() to check
  if fn returns True for any element in the list

https://www.30secondsofcode.org/python/s/some
'''

def some(lst, fn = lambda x: x):
    return any(map(fn, lst))
  

# Example
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True



