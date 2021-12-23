
'''
byte_size
Returns the length of a string in bytes

- Use str.encode('utf-8') to encode the given string and return its length

https://www.30secondsofcode.org/python/s/byte-size
'''

def byte_size(s):
    return len(s.encode('utf-8'))


# Example
byte_size('😀')          # 4
byte_size('Hello World')  # 11
