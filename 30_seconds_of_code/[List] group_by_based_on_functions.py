'''
group_by
Groups the elements of a list based on the given function

- Use collections.defaultdict to initialize a dictionary
- Use fn in combination with a for loop and dict.append() to populate the dictionary
- Use dict() to convert it to a regular dictionary

https://www.30secondsofcode.org/python/s/group-by
'''

from collections import defaultdict

def group_by(lst, func):
    cnt = defaultdict(list)
    for el in lst:
        cnt[func(el)].append(el)
    return dict(cnt)
    

# Example
from math import floor

group_by([6.1, 4.2, 6.3], floor)       # {6: [6.1, 6.3], 4: [4.2]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}

