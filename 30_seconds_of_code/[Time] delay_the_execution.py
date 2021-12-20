
'''
delay
Invokes the provided function after ms milliseconds

- Use time.sleep() to delay the execution of fn by ms / 1000 seconds

https://www.30secondsofcode.org/python/s/delay
'''

from time import sleep

def delay(fn, ms, *args):
    sleep(ms/1000)
    return fn(*args)


# Example
delay(lambda x: print(x), 1000, 'later')
# prints 'later' after one second
