'''
sample
Returns a random element from a list

- Use random.choice() to get a random element from lst

https://www.30secondsofcode.org/python/s/sample
'''

from random import choice

def sample(lst):    
    return choice(lst)


# Example
sample([3, 7, 9, 11]) # 9
