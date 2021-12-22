
'''
all_equal
Checks if all elements in a list are equal

- Use set() to eliminate duplicate elements
  and then use len() to check if length is 1

https://www.30secondsofcode.org/python/s/all-equal
'''

def all_equal(lst):
    return len(set(lst)) == 1


# Example
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
