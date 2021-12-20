
'''
fibonacci
Generates a list, containing the Fibonacci sequence, up until the nth term

- Starting with 0 and 1, use list.append() to add the sum of the last two numbers of the list to the end of the list, until the length of the list reaches n.
- If n is less or equal to 0, return a list containing 0.

https://www.30secondsofcode.org/python/s/fibonacci
'''

def fibonacci(n):
    if n <= 0:
        return [0]
    rst = [0, 1]
    while len(rst) <= n:
        next_v = rst[len(rst)-2] + rst[len(rst)-1]
        rst.append(next_v)
    return rst


# Example
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
