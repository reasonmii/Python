'''
1) max_element_index
Returns the index of the element with the maximum value in a list

- Use max() and list.index() to get the maximum value
  in the list and return its index

https://www.30secondsofcode.org/python/s/max-element-index
'''

def max_element_index(lst):
    return lst.index(max(lst))


# Example
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4


'''
2) min_element_index
Returns the index of the element with the minimum value in a list

- Use min() and list.index() to obtain the minimum value
  in the list and then return its index

https://www.30secondsofcode.org/python/s/min-element-index
'''

def min_element_index(lst):
  return lst.index(min(lst))


# Example
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
