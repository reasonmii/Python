
'''
chunk
Chunks a list into smaller lists of a specified size

- Use list() and range() to create a list of the desired size
- Use map() on the list and fill it with splices of the given list

https://www.30secondsofcode.org/python/s/chunk
'''

from math import ceil

def chunk(lst, size):
    return list(map(lambda x: lst[x * size : x * size + size],
                    list(range(ceil(len(lst) / size)))))

    
# Example
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]


# reference =====================================================

ceil(5/2)   # 3
ceil(10/3)  # 4

lst = [1,2,3,4,5]
list(range(ceil(len(lst) / 2)))  # [0, 1, 2]



