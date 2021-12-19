
'''
none
Checks if the provided function returns True for at least one element in the list

- Use all() and fn to check if fn returns False for all the elements in the list

all
- Return True if bool(x) is True for all values x in the iterable
    
https://www.30secondsofcode.org/python/s/none
'''

def none(lst, fn = lambda x: x):
    return all(not fn(x) for x in lst)


# Example
none([0, 1, 2, 0], lambda x: x >= 2 ) # False
none([0, 0, 0]) # True
