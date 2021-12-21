'''
1) key_of_max
Finds the key of the maximum value in a dictionary

- Use max() with the key parameter set to dict.get() to find
  and return the key of the maximum value in the given dictionary

https://www.30secondsofcode.org/python/s/key-of-max
'''

def key_of_max(d):
  return max(d, key=d.get())


# Example
key_of_max({'a':4, 'b':0, 'c':13}) # c


'''
2) key_of_min
Finds the key of the minimum value in a dictionary

- Use min() with the key parameter set to dict.get() to find
  and return the key of the minimum value in the given dictionary

https://www.30secondsofcode.org/python/s/key-of-min
'''

def key_of_min(d):
  return min(d, key=d.get())

# Example
key_of_min({'a':4, 'b':0, 'c':13}) # b


