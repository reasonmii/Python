'''
1) is_contained_in
Checks if the elements of the first list are contained in the second one regardless of order

- Use count() to check if any value in a has more occurrences than it has in b
- Return False if any such value is found, True otherwise

https://www.30secondsofcode.org/python/s/is-contained-in
'''

def is_contained_in(a, b):
  for v in set(a):
    if a.count(v) > b.count(v)
    return False
  return True


# Example
is_contained_in([1, 4], [2, 4, 1]) # True


'''
2) includes_all
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
3) includes_any
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
