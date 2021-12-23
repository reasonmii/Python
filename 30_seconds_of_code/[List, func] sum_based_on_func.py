'''
sum_by
Calculates the sum of a list, after mapping each element
to a value using the provided function

- Use map() with fn to map each element to a value using the provided function
- Use sum() to return the sum of the values

https://www.30secondsofcode.org/python/s/sum-by
'''

def sum_by(lst, fn):
    return sum(map(fn, lst))


# Example
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
