
'''
geometric_progression
Initializes a list containing the numbers in the specified range
where start and end are inclusive and "the ratio between two terms is step"
Returns an error if step equals 1

- Use range(), math.log() and math.floor() and a list comprehension
  to create a list of the appropriate length, applying the step for each element
- Omit the second argument, start, to use a default value of 1
- Omit the third argument, step, to use a default value of 2

https://www.30secondsofcode.org/python/s/geometric-progression
'''

from math import floor, log

def geometric_progression(end, start=1, step=2):
    s = floor(log(end/start)/log(step))
    return [start * step ** i for i in range(s + 1)]
  

# Example
geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]


# reference =====================================================

floor(log(256/1)/log(2))  # 8
floor(log(256/3)/log(2))  # 6
floor(log(256/3)/log(4))  # 3

