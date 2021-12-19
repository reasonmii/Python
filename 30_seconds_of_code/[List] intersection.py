
'''
similarity
Returns a list of elements that exist in both lists

- Use a list comprehension on a to only keep values contained in both lists

https://www.30secondsofcode.org/python/s/similarity
'''

def similarity(a, b):
    return [x for x in a if x in b]


# Example
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
