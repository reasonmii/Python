
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


# reference =====================================================

a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
a.update({'bob':99, 'tony':99, 'kim': 30})

a
# {'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}
