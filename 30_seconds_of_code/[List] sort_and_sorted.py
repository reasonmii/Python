
'''
Main Difference
1) sorted() will return a new sorted list leaving the original list unchanged
2) sorted() accepts any iterable while list.sort() can only be used with lists

When to use
- list.sort() should be used whenever mutating the list is intended
  and retrieving the original order of the elements is not desired
- sorted() should be used when the object to be sorted is an iterable
  (e.g. list, tuple, dictionary, string)
  and the desired outcome is a sorted list containing all elements
  
https://www.30secondsofcode.org/articles/s/python-sortedlist-vs-list-sort  
'''

nums = [2, 3, 1, 5, 6, 4, 0]

print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print(nums)           # [2, 3, 1, 5, 6, 4, 0]

print(nums.sort())    # None
print(nums)           # [0, 1, 2, 3, 4, 5, 6]

