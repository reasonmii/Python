'''
initialize_list_with_range
Initializes a list containing the numbers in the specified range
where start and end are inclusive with their common difference step

- Use list() and range() to generate a list of the appropriate length,
  filled with the desired values in the given range
- Omit start to use the default value of 0
- Omit step to use the default value of 1

https://www.30secondsofcode.org/python/s/initialize-list-with-range
'''

def initialize_list_with_range(end, start=0, step=1):
  return list(range(start, end+1, step))


# Example
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
