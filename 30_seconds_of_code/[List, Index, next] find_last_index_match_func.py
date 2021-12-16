'''
find_last_index
Finds the index of the last element in the given list
that satisfies the provided testing function

- Use a list comprehension, enumerate() and next()
  to return the index of the last element in lst for which fn returns True

https://www.30secondsofcode.org/python/s/find-last-index
'''

def find_last_index(lst, fn):
    return len(lst) - 1 - next(idx for idx, item in enumerate(lst[::-1]) if fn(item))
     

# Example
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2

