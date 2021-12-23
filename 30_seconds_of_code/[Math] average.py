'''
average
Calculates the average of two or more numbers

- Use sum() to sum all of the args provided, divide by len()

https://www.30secondsofcode.org/python/s/average
'''

def average(*args):
    return sum(args, 0.0) / len(args)


# Example
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
