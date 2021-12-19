'''
most_frequent
Returns the most frequent element in a list

- Use set() to get the unique values in lst
- Use max() to find the element that has the most appearances

https://www.30secondsofcode.org/python/s/most-frequent
'''

def most_frequent(lst):
    return max(set(lst), key = lst.count)


# Example
most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2
