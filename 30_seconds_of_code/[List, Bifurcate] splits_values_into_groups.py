
'''
bifurcate
Splits values into two groups, based on the result of the given filter list

- Use a list comprehension and zip() to add elements to groups, based on filter
- If filter has a truthy value for any element,
  add it to the first group, otherwise add it to the second group

https://www.30secondsofcode.org/python/s/bifurcate
'''

def bifurcate(lst, filter):
    return [[x for x, flag in zip(lst, filter) if flag],
            [x for x, flag in zip(lst, filter) if not flag]]


# Example
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# [ ['beep', 'boop', 'bar'], ['foo'] ]


# reference =====================================================

lst = zip(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])

for pair in lst:
    print(pair)
# ('beep', True)
# ('boop', True)
# ('foo', False)
# ('bar', True)
