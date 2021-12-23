'''
1) intersection
Returns a list of elements that exist in both lists

- Create a set from a and b
- Use the built-in set operator & to only keep values contained in both sets,
  then transform the set back into a list

https://www.30secondsofcode.org/python/s/intersection
'''

def intersection(a, b):
    _a, _b = set(a), set(b)
    return list(_a & _b)


# Example
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]


'''
2) similarity
Returns a list of elements that exist in both lists

- Use a list comprehension on a to only keep values contained in both lists

https://www.30secondsofcode.org/python/s/similarity
'''

def similarity(a, b):
    return [x for x in a if x in b]


# Example
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]


