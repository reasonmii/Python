
'''
have_same_contents
Checks if two lists contain the same elements regardless of order

- Use set() on the combination of both lists to find the unique values
- Iterate over them with a for loop comparing the count() of each unique value in each list
- Return False if the counts do not match for any element, True otherwise

https://www.30secondsofcode.org/python/s/have-same-contents
'''

def have_same_contents(a, b):
    for v in set(a + b):
        if a.count(v) != b.count(v):
            return False
    return True


# Example
have_same_contents([1, 2, 4], [2, 4, 1]) # True


# reference =====================================================

a = [1, 1, 2, 3]
b = [2, 3, 1]

for v in set(a + b):
    print(v)
# 1
# 2
# 3

a.count(1)   # 2



