
'''
1) pad
Pads a string on both sides with the specified character,
if it's shorter than the specified length

- Use str.ljust() and str.rjust() to pad both sides of the given string
- Omit the third argument, char, to use the whitespace character
  as the default padding character

https://www.30secondsofcode.org/python/s/pad
'''

from math import floor

def pad(s, n, char=' '):
  return s.rjust(floor((len(s) + n)/2), char).ljust(n, char)


# Example
pad('cat', 8) # '  cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'


'''
2) pad_number
Pads a given number to the specified length

- Use str.zfill() to pad the number to the specified length,
  after converting it to a string

https://www.30secondsofcode.org/python/s/pad-number
'''

def pad_number(n, p):
    return str(n).zfill(p)


# Example
pad_number(1234, 6) # '001234'

