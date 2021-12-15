
'''
bifurcate_by
Splits values into two groups, based on the result of the given filtering function

- Use a list comprehension to add elements to groups,
  based on the value returned by fn for each element
- If fn returns a truthy value for any element,
  add it to the first group, otherwise add it to the second group

https://www.30secondsofcode.org/python/s/bifurcate-by
'''

def bifurcate_by(lst, fn):
    return [[x for x in lst if fn(x)],
            [x for x in lst if not fn(x)]]
    

# Example
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]

