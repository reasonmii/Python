
'''
arithmetic_progression
Generates a list of numbers in the arithmetic progression
starting with the given positive integer and up to the specified limit

- Use range() and list() with the appropriate start, step and end values

https://www.30secondsofcode.org/python/s/arithmetic-progression
'''

def arithmetic_progression(a, b):
    return list(range(a, b+1, a))


# Example
arithmetic_progression(5, 25) # [5, 10, 15, 20, 25] 
