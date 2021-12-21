'''
min_element_index
Returns the index of the element with the minimum value in a list

- Use min() and list.index() to obtain the minimum value
  in the list and then return its index

https://www.30secondsofcode.org/python/s/min-element-index
'''

def min_element_index(lst):
  return lst.index(min(lst))


# Example
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
