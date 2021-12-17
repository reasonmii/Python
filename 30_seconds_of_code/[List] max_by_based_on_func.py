
'''
max_by
Returns the maximum value of a list,
after mapping each element to a value using the provided function

- Use map() with fn to map each element to a value using the provided function
- Use max() to return the maximum value

https://www.30secondsofcode.org/python/s/max-by
'''

def max_by(lst, fn):
    return max(map(fn, lst))


# Example
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
