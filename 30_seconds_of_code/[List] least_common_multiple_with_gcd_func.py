
'''
lcm
Returns the least common multiple of a list of numbers

- Use functools.reduce(), math.gcd()
  and lcm(x,y) = x * y / gcd(x,y) over the given list

gcd
- greatest common divisor 최대 공약수

https://www.30secondsofcode.org/python/s/lcm
'''

from functools import reduce
from math import gcd

def lcm(numbers):
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)
    

# Example
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60


# reference =====================================================

gcd(60, 100)  # 20



