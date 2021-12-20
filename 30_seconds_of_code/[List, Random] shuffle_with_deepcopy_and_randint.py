'''
shuffle
Randomizes the order of the values of an list, returning a new list

- Uses the Fisher-Yates algorithm to reorder the elements of the list
- random.shuffle provides similar functionality to this snippet

Fisher-Yates shuffle
- It is an algorithm for generating a random permutation of a finite sequence
- It shuffles the sequence

https://www.30secondsofcode.org/python/s/shuffle
'''

from copy import deepcopy
from random import randint

def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]    
    return temp_lst
        

# Example
foo = [1, 2, 3]
shuffle(foo)   # [2, 3, 1]

