
'''
find_parity_outliers
Finds the items that are parity outliers in a given list

- Use collections.Counter with a list comprehension to count even and odd values in the list
- Use collections.Counter.most_common() to get the most common parity
- Use a list comprehension to find all elements that do not match the most common parity

https://www.30secondsofcode.org/python/s/find-parity-outliers
'''

from collections import Counter

def find_parity_outliers(nums):
    rst = Counter([n % 2 for n in nums]).most_common()[0][0]
    return [x for x in nums if x % 2 != rst]


# Example
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]

