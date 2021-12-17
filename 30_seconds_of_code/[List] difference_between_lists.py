
'''
difference
Calculates the difference between two iterables, without filtering duplicate values

- Create a set from b
- Use a list comprehension on a to only keep values
  not contained in the previously created set, _b

https://www.30secondsofcode.org/python/s/difference
'''

def difference(a, b):
    _b = set(b)
    return [item for item in a if item not in _b]


# Example
difference([1, 2, 3], [1, 2, 4]) # [3]

