'''
Python slice notation
https://www.30secondsofcode.org/articles/s/python-slice-notation

1. Basic syntax
- It is used to return a list or a portion of a list

[start : stop : step]
- start : index of the first item (included) (default : 0)
- stop : index before stop (not included) (default : len(nums))
- step : stride between any two items (default : 1)
- All three of the arguments are optional
- An idiomatic way to shallow clone a list would be using [:] (e.g. nums_clone = nums[:])
'''

nums = [1, 2, 3, 4, 5]

nums[1:4]     # [2, 3, 4]       (start at 0, stop before 4)
nums[2:]      # [3, 4, 5]       (start at 0, stop at end of list)
nums[:3]      # [1, 2, 3]       (start at 0, stop before 3)
nums[1:4:2]   # [2, 4]          (start at 1, stop before 4, every 2nd element)
nums[2::2]    # [3, 5]          (start at 2, stop at end of list, every 2nd element)
nums[:3:2]    # [1, 3]          (start at 0, stop before 3, every 2nd element)
nums[::2]     # [1, 3, 5]       (start at 0, stop at end of list, every 2nd element)
nums[::]      # [1, 2, 3, 4, 5] (start at 0, stop at end of list)

'''
2. Negative values
- It means counting from the end of the list (e.g. -1 would represent the last element)

A negative step
- The list is sliced in reverse (from end to start)
- 'start' should be greater than 'stop'
- 'stop' is more like 'stop_after' if you are looking at the list non-reversed
'''

nums = [1, 2, 3, 4, 5]

nums[1:-2]    # [2, 3]      (start at 1, stop before 2nd to last)
nums[-3:-1]   # [3, 4]      (start at 3rd to last, stop before last)

nums[::-1]    # [5, 4, 3, 2, 1]   (reversed)
nums[4:1:-1]  # [5, 4, 3]         (reversed, start at 4, stop after 1)
nums[-1:1:-2] # [5, 3]            (reversed, start at last, stop after 1, every 2nd)

'''
3. Empty slices
- you'll get an empty list if the arguments' values are out of the list's range
'''

nums = [1, 2, 3, 4, 5]

nums[6:8]     # []
nums[:-10]    # []
