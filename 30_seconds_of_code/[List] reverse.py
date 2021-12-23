'''
reverse
Reverses a list or a string

- Use slice notation to reverse the list or string

https://www.30secondsofcode.org/python/s/reverse
'''

def reverse(obj):
    return obj[::-1]


# Example
reverse([1, 2, 3]) # [3, 2, 1] 
reverse('snippet') # 'teppins' 
