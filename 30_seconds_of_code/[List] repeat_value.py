
'''
initialize_list_with_values
Initializes and fills a list with the specified value

- Use a list comprehension and range() to generate a list of length equal to n,
filled with the desired values
- Omit val to use the default value of 0

https://www.30secondsofcode.org/python/s/initialize-list-with-values
'''

def initialize_list_with_values(n, val=0):
    return [val for x in range(n)]


# Example
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
