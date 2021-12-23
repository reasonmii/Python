
'''
clamp_number
Clamps num within the inclusive range specified by the boundary values

- If num falls within the range (a, b), return num
- Otherwise, return the nearest number in the range

https://www.30secondsofcode.org/python/s/clamp-number
'''

def clamp_number(num, a, b):
    return max(min(num, max(a, b)), min(a, b))


# Example
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
