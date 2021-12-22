'''
is_prime
Checks if the provided integer is a prime number

- Return False if the number is 0, 1, a negative number or a multiple of 2
- Use all() and range() to check numbers from 3 to the square root of the given number
- Return True if none divides the given number, False otherwise

all
- 한 개라도 False, 0 이면 False 반환
- 전체가 True, >= 1 일 때, True 반환

https://www.30secondsofcode.org/python/s/is-prime
'''

from math import sqrt

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


# Example
is_prime(11) # True

