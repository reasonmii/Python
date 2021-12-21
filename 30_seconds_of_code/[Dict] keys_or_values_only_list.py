
'''
1) keys_only
Creates a flat list of all the keys in a flat dictionary

- Use dict.keys() to return the keys in the given dictionary
- Return a list() of the previous result

https://www.30secondsofcode.org/python/s/keys-only
'''

def keys_only(d):
    return list(d.keys())


# Example
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}

keys_only(ages) # ['Peter', 'Isabel', 'Anna']


'''
2) values_only
Returns a flat list of all the values in a flat dictionary

- Use dict.values() to return the values in the given dictionary
- Return a list() of the previous result

https://www.30secondsofcode.org/python/s/values-only
'''

def values_only(d):    
    return list(d.values())


# Example
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}

values_only(ages) # [10, 11, 9]
