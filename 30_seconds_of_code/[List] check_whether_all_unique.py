
'''
1) all_unique
Checks if all the values in a list are unique

- Use set() on the given list to keep only unique occurrences
- Use len() to compare the length of the unique values to the original list

https://www.30secondsofcode.org/python/s/all-unique
'''

def all_unique(lst):
    return len(lst) == len(set(lst))


# Example
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False


'''
2) has_duplicates
Checks if there are duplicate values in a flat list

- Use set() on the given list to remove duplicates,
  compare its length with the length of the list

https://www.30secondsofcode.org/python/s/has-duplicates
'''

def has_duplicates(lst):
    return len(lst) != len(set(lst))


# Example
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x) # True
has_duplicates(y) # False

