'''
compact
Removes falsy values from a list

- Use filter() to filter out falsy values
  (False, None, 0, and "")

★ None will remove any falsey values like [], {} 0 etc

https://www.30secondsofcode.org/python/s/compact
'''

def compact(lst):
    return list(filter(None, lst))


# Example
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
