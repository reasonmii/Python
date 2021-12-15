
'''
What are named tuples in Python?
https://www.30secondsofcode.org/articles/s/python-named-tuples

Python's named tuples are a very simple yet interesting feature that can make a developer's life easier

특징
- Part of the "collections module"
- Very similar to regular tuples
- Specify field names as a list or comma/space-separated string
- Accessed using "field names" instead of indexes

ex) a point in the two-dimensional plane can be represented using two coordinates
- Regular tuple : accessed by index ([0] and [1])
- Named tuple : accessed by x and y (we can still use indexes, too, if we want)

장점
- Increased readability of your code
- Allow for default values to be specified via the defaults iterable argument
- Automatically rename duplicate or invalid fields via the rename boolean argument

단점
- As named tuple instances do not have per-instance dictionaries,
  meaning they require as much memory as regular tuples
'''

from collections import namedtuple

# Regular tuple
p = (2, 4)
print(p[0], p[1])  # 2 4

# Named tuple example1
point = namedtuple('Point', 'x y')
p = point(3, 5)
print(p.x, p.y)    # 3 5
print(p[0], p[1])  # 3 5

# Named tuple example2
point = namedtuple('Point', ['x', 'y', 'z'], defaults=[1])

a = point(1, 1, 0)
print(a.x, a.y, a.z)   # 1 1 0

b = point(2, 2)
print(b.x, b.y, b.z)  # 2 2 1

