'''
find_index_of_all
Finds the indexes of all elements in the given list
that satisfy the provided testing function

- Use enumerate() and a list comprehension to return the indexes
  of the all element in lst for which fn returns True

https://www.30secondsofcode.org/python/s/find-index-of-all
'''

def find_index_of_all(lst, fn):
    return [idx for idx, x in enumerate(lst) if fn(x)]


# Example
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
