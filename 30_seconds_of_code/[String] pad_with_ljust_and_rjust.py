
'''
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

