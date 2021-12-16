
'''
find
Finds the value of the first element in the given list
that satisfies the provided testing function

- Use a list comprehension and next() to return the first element in lst
  for which fn returns True

https://www.30secondsofcode.org/python/s/find
'''

def find(lst, fn = lambda x: x):
    return next(x for x in lst if fn(x))


# Example
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
