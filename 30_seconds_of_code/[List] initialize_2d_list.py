
'''
initialize_2d_list
Initializes a 2D list of given width and height and value

- Use a list comprehension and range() to generate h rows
  where each is a list with length h, initialized with val
- Omit the last argument, val, to set the default value to None

https://www.30secondsofcode.org/python/s/initialize-2-d-list
'''

def initialize_2d_list(w, h, val=None):
    return [[val for x in range(w)] for y in range(h)]


# Example
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
