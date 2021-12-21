'''
They are used for different comparison purposes and yield different results

1) == : equality operator
- checks for "value equality"
- evaluate to True if the two objects "have the same value"

2) 'is' keyword : identity operator
- checks for "reference equality"
- return True if two variables both refer to "the same object" in memory (aka. identity)
'''

a = [1, 2, 3]
b = a
c = [x for x in a]

print([
  a == b, # True
  a is b, # True
  a == c, # True
  a is c  # False
])

x = 'hi'
y = x
z = 'HI'.lower()

print([
  x == y, # True
  x is y, # True
  x == z, # True
  x is z  # False
])

