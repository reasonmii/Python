
'''
weighted_average
Returns the weighted average of two or more numbers

- Use sum() to sum the products of the numbers by their weight and to sum the weight
- Use zip() and a list comprehension to iterate over the pairs of values and weights

https://www.30secondsofcode.org/python/s/weighted-average
'''

def weighted_average(nums, weights):
    return sum(n * w for n, w in zip(nums, weights)) / sum(weights)

            
# Example
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
