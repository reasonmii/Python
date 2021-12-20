'''
max_element_index
Returns the index of the element with the maximum value in a list

- Use max() and list.index() to get the maximum value
  in the list and return its index

https://www.30secondsofcode.org/python/s/max-element-index
'''

def max_element_index(lst):
    return lst.index(max(lst))


# Example
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
