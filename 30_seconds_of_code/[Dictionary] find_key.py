'''
1) find_key
Finds the first key in the provided dictionary that has the given value

- Use dictionary.items() and next() to return the first key
  that has a value equal to val

https://www.30secondsofcode.org/python/s/find-key
'''

def find_key(d, val):
  return next(k for k, v in d.items() if v == val)


# Example
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}

find_key(ages, 11) # 'Isabel'


'''
2) find_keys
Finds all keys in the provided dictionary that have the given value

- Use dictionary.items(), a generator and list() to return all keys
  that have a value equal to val

https://www.30secondsofcode.org/python/s/find-keys
'''

def find_keys(dic, val):
    return list(key for key, v in dic.items() if v == val)


# Example
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}

find_keys(ages, 10) # [ 'Peter', 'Anna' ]
