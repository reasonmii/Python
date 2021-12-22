
'''
key_in_dict
Checks if the given key exists in a dictionary

- Use the in operator to check if d contains key

https://www.30secondsofcode.org/python/s/key-in-dict
'''

def key_in_dict(d, key):
    return (key in d)


# Example
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
