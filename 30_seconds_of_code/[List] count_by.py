'''
count_by
Groups the elements of a list based on the given function
and returns the count of elements in each group

- Use collections.defaultdict to initialize a dictionary
- Use map() to map the values of the given list using the given function
- Iterate over the map and increase the element count each time it occurs

https://www.30secondsofcode.org/python/s/count-by

defaultdict(int)
- default 값이 int인 dictionary
'''

from collections import defaultdict

def count_by(lst, func):
    cnt = defaultdict(int)
    for val in map(func, lst):
        cnt[val] += 1
    return dict(cnt)


# Example
from math import floor

count_by([6.1, 4.2, 6.3], floor)       # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}

