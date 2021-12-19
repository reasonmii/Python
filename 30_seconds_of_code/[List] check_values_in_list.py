'''
1) includes_all
Checks if all the elements in values are included in lst

- Check if every value in values is contained in lst using a for loop
- Return False if any one value is not found, True otherwise

https://www.30secondsofcode.org/python/s/includes-all
'''

def includes_all(lst, values):
    for v in values:
        if v not in lst:
            return False
    return True


# Example
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False


'''
2) includes_any
Checks if any element in values is included in lst

- Check if any value in values is contained in lst using a for loop
- Return True if any one value is found, False otherwise

https://www.30secondsofcode.org/python/s/includes-any
'''

def includes_any(lst, values):
    for v in values:
        if v in lst:
            return True
    return False


# Example
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
