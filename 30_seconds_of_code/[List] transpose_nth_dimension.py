
'''
transpose
Transposes a two-dimensional list

- Use *lst to get the provided list as tuples
- Use zip() in combination with list() to create the transpose of the given two-dimensional list

https://www.30secondsofcode.org/python/s/transpose
'''

def transpose(lst):    
    return list(zip(*lst))


# Example
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]


# reference =====================================================

for x in zip([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]):
    print(x)
# (1, 4, 7, 10)
# (2, 5, 8, 11)
# (3, 6, 9, 12)

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

for x in zip(*a):
    print(x)
# (1, 4, 7, 10)
# (2, 5, 8, 11)
# (3, 6, 9, 12)
