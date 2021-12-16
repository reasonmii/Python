
'''
pluck
Converts a list of dictionaries into a list of values
corresponding to the specified key

- Use a list comprehension and dict.get()
  to get the value of key for each dictionary in lst

https://www.30secondsofcode.org/python/s/pluck
'''

def pluck(lst, key):
    return [x.get(key) for x in lst]


# Example
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name': 'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]

pluck(simpsons, 'age') # [8, 36, 34, 10]

