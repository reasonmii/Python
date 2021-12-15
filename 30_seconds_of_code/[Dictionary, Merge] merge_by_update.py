
'''
merge_dictionaries
Merges two or more dictionaries

- Create a new dict and loop over dicts, using dictionary.update()
  to add the key-value pairs from each one to the result

https://www.30secondsofcode.org/python/s/merge-dictionaries
'''

def merge_dictionaries(*dicts):
    rst = dict()
    for d in dicts:
        rst.update(d)
    return rst


# Example
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}

ages_two = {
  'Anna': 9
}

merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
