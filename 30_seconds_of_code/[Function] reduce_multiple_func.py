'''
compose
Performs right-to-left function composition

- Use functools.reduce() to perform right-to-left function composition
- The last (rightmost) function can accept one or more arguments;
  the remaining functions must be unary

※ unary : 단항의, 1진법의

https://www.30secondsofcode.org/python/s/compose
'''

from functools import reduce

def compose(*fns):
    return reduce(lambda f, g: lambda *args: f(g(*args)), fns)


# Example
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15


'''
compose_right
Performs left-to-right function composition

- Use functools.reduce() to perform left-to-right function composition
- The first (leftmost) function can accept one or more arguments;
  the remaining functions must be unary

https://www.30secondsofcode.org/python/s/compose-right
'''

from functools import reduce

def compose_right(*fns):
    return reduce(lambda f, g: lambda *args: g(f(*args)), fns)


# Example
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9

