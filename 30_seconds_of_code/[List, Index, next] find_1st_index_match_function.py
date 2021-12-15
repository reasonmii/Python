
'''
find_index
Finds the index of the first element in the given list
that satisfies the provided testing function

- Use a list comprehension, enumerate() and next()
  to return the index of the first element in lst for which fn returns True

https://www.30secondsofcode.org/python/s/find-index
'''

def find_index(lst, fn):
    return next(idx for idx, x in enumerate(lst) if fn(x))


# Example
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0


# reference =====================================================
# iter는 객체의 __iter__ method 호출
# next는 객체의 __next__ method 호출

a = iter(range(3))
# <range_iterator at 0x15062f35550>

next(a)
# 0
# 1
# 2
