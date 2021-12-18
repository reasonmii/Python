
'''
dict_to_list
Converts a dictionary to a list of tuples.

- Use dict.items() and list() to get a list of tuples from the given dictionary

https://www.30secondsofcode.org/python/s/dict-to-list
'''

def dict_to_list(d):
    return list(d.items())


# Example
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}

dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]


# reference =====================================================

d.items()
# dict_items([('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)])


