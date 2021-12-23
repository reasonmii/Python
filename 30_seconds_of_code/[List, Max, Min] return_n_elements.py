
'''
1) max_n
Returns the n maximum elements from the provided list

- Use sorted() to sort the list
- Use slice notation to get the specified number of elements
- Omit the second argument, n, to get a one-element list.
- If n is greater than or equal to the provided list's length,
  then return the original list (sorted in descending order)

https://www.30secondsofcode.org/python/s/max-n
'''

def max_n(lst, n=1):
    return sorted(lst, reverse=True)[:n]

            
# Example
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
max_n([1, 2, 3], 4) # [3, 2]


'''
2) min_n
Returns the n minimum elements from the provided list

- Use sorted() to sort the list.
- Use slice notation to get the specified number of elements
- Omit the second argument, n, to get a one-element list
- If n is greater than or equal to the provided list's length,
  then return the original list (sorted in ascending order)

https://www.30secondsofcode.org/python/s/min-n
'''

def min_n(lst, n=1):
    return sorted(lst)[:n]

            
# Example
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
