
'''
binomial_coefficient
Calculates the number of ways to choose k items from n items
without repetition and without order

- Use math.comb() to calculate the binomial coefficient

★ math.comb(n, k) = nCk

https://www.30secondsofcode.org/python/s/binomial-coefficient
'''

from math import comb

def binomial_coefficient(n, k):
    return comb(n, k)


# Example
binomial_coefficient(8, 2) # 28
