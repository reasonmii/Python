
'''
factorial
Calculates the factorial of a number

- Use recursion
- If num is less than or equal to 1, return 1
- Otherwise, return the product of num and the factorial of num - 1
- Throws an exception if num is a negative or a floating point number

https://www.30secondsofcode.org/python/s/factorial
'''

def factorial(n):
    if not ((n >= 0) and (n % 1 == 0)):
        # 예외 발생
        raise Exception("Number can't be floating point or negative")
    return 1 if n <= 1 else n * factorial(n-1)


# Example
factorial(6) # 720

