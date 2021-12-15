
'''
Creates a list with the unique values filtered out

- Use collections.Counter to get the count of each value in the list.
- Use a list comprehension to create a list containing only the non-unique values.

https://www.30secondsofcode.org/python/s/filter-unique
'''

from collections import Counter

def filter_non_unique(lst):
    return [item for item, count in Counter(lst).items() if count > 1]


# Example
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]


# reference =====================================================

Counter([1, 2, 2, 3, 4, 4, 5])
# Counter({1: 1, 2: 2, 3: 1, 4: 2, 5: 1})

Counter([1, 2, 2, 3, 4, 4, 5]).items()
# dict_items([(1, 1), (2, 2), (3, 1), (4, 2), (5, 1)])

for item, count in Counter([1, 2, 2, 3, 4, 4, 5]).items():
    print(item, count)
# 1 1
# 2 2
# 3 1
# 4 2
# 5 1

