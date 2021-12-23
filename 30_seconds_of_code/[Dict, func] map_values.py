'''
map_dictionary
Maps the values of a list to a dictionary using a function,
where the key-value pairs consist of the original value as the key
and the result of the function as the value

- Use map() to apply fn to each value of the list
- Use zip() to pair original values to the values produced by fn
- Use dict() to return an appropriate dictionary

https://www.30secondsofcode.org/python/s/map-dictionary
'''

def map_dictionary(lst, fn):
    return dict(zip(lst, map(fn, lst)))
        

# Example
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }

