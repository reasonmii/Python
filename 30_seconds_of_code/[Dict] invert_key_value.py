
'''
invert_dictionary
Inverts a dictionary with unique hashable values

- Use dictionary.items() in combination with a list comprehension
  to create a new dictionary with the values and keys inverted

https://www.30secondsofcode.org/python/s/invert-dictionary
'''

def invert_dictionary(obj):
    return { v : k for k, v in obj.items() }


# Example
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}

invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
