
'''
spread
Flattens a list, by spreading its elements into a new list.

- Loop over elements, use list.extend() if the element is a list,
  list.append() otherwise

https://www.30secondsofcode.org/python/s/spread
'''

def spread(arg):
    rst = []
    for i in arg:
        rst.extend(i) if isinstance(i, list) else rst.append(i)
    return rst


# Example
spread([1, 2, 3, [4, 5, 6], [7], 8, 9])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
