'''
digitize
Converts a number to a list of digits

- Use map() combined with int on the string representation of n
- Return a list from the result

https://www.30secondsofcode.org/python/s/digitize
'''

def digitize(num):
    return list(map(int, str(num)))

    
# Example
digitize(123) # [1, 2, 3]
