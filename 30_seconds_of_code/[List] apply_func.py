'''
for_each_right
Executes the provided function once for each list element,
starting from the list's last element

- Use a for loop in combination with slice notation to execute fn
  for each element in itr, starting from the last one

https://www.30secondsofcode.org/python/s/for-each-right
'''

def for_each_right(itr, fn):
    for el in itr[::-1]:
        fn(el)


# Example
for_each_right([1, 2, 3], print) # 3 2 1
