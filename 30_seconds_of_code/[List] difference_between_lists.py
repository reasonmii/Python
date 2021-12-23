
'''
1) difference
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


'''
2) symmetric_difference
Returns the symmetric difference between two iterables,
without filtering out duplicate values

- Create a set from each list
- Use a list comprehension on each of them to only keep values
  not contained in the previously created set of the other

https://www.30secondsofcode.org/python/s/symmetric-difference
'''

def symmetric_difference(a, b):
    (_a, _b) = (set(a), set(b))
    return [item for item in a if item not in _b] + [item for item in b if item not in _a]
  

# Example
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
