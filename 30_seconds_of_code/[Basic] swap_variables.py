'''
3 ways to swap two variables in Python
https://www.30secondsofcode.org/articles/s/python-swap-variables

1. Using a temporary variable
- The simplest way
'''

a = 11
b = 7

temp = a
a = b
b = temp

print(a) # 7
print(b) # 11

'''
2. Tuple swap : Without a temporary variable
- Use tuple packing and sequence unpacking
- Tuples can be constructed in a number of ways (e.g. separating tuple items using "comma")
- ★ Python evaluates the right-hand side of an assignment before its left-hand side
- So, by separating the variables with commas on the right side of the statement
  the variables are packed into a tuple
  and unpacked by placing the same number of comma-separated target variables on the left side
- It can be used for more than two variables as long as the same number of variables are on both sides of the statement
'''

a = 11
b = 7

a, b = b, a

print(a) # 7
print(b) # 11

'''
3. Using arithmetic operators (for numbers only)
- arithmetic operators : addition, subtraction, multiplication and division (+, -, *, /)
- It is based on calculating and then swapping them using the sum and the difference from the sum
'''

a = 11
b = 7

a = a + b   # a = 18, b = 7
b = a - b   # a = 18, b = 11
a = a - b   # a = 7,  b = 11

print(a) # 7
print(b) # 11
