
'''
get
Retrieves the value of the nested key
indicated by the given selector list from a dictionary or list

- Use functools.reduce() to iterate over the selectors list
- Apply operator.getitem() for each key in selectors,
  retrieving the value to be used as the iteratee for the next iteration

https://www.30secondsofcode.org/python/s/get
'''

from functools import reduce
from operator import getitem

def get(dic, selectors):
    return reduce(getitem, selectors, dic)    


# Example
users = {
  'freddy': {'name': {'first': 'fred', 'last': 'smith'},
             'postIds': [1, 2, 3]}}

get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2


# reference =====================================================

help(reduce)
# reduce(function, sequence[, initial]) -> value
# Apply a function of two arguments cumulatively to the items of a sequence,
# from left to right, so as to reduce the sequence to a single value
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)

