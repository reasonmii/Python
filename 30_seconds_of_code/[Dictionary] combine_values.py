'''
combine_values
Combines two or more dictionaries, creating a list of values for each key

- Create a new collections.defaultdict with list as the default value for each key and loop over dicts
- Use dict.append() to map the values of the dictionary to keys
- Use dict() to convert the collections.defaultdict to a regular dictionary

https://www.30secondsofcode.org/python/s/combine-values
'''

from collections import defaultdict

def combine_values(*dicts):
    dic = defaultdict(list)
    for d in dicts:
        for key in d:
            dic[key].append(d[key])
    return dict(dic)


# Example
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
