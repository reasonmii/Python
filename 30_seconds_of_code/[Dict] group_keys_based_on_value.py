'''
collect_dictionary
Inverts a dictionary with non-unique hashable values

- Create a collections.defaultdict with list as the default value for each key
- Use dictionary.items() in combination with a loop
  to map the values of the dictionary to keys using dict.append()
- Use dict() to convert the collections.defaultdict to a regular dictionary

https://www.30secondsofcode.org/python/s/collect-dictionary
'''

from collections import defaultdict

def collect_dictionary(obj):
    dic = defaultdict(list)
    for k, v in obj.items():
        dic[v].append(k)
    return dict(dic)    


# Example
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}

collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }

