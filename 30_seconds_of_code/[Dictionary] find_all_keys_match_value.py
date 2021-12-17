
'''
find_keys
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
