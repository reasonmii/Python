'''
1. Python slice notation
https://www.30secondsofcode.org/articles/s/python-slice-notation

1) Basic syntax
- It is used to return a list or a portion of a list

[start_at : stop_before : step]
- start_at : index of the first item (included) (default : 0)
- stop_before : index before stop (not included) (default : len(nums))
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
2) Negative values
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
3) Empty slices
- you'll get an empty list if the arguments' values are out of the list's range
'''

nums = [1, 2, 3, 4, 5]

nums[6:8]     # []
nums[:-10]    # []


'''
2. Python slice notation
https://www.30secondsofcode.org/articles/s/python-slice-assignment

1) Basic syntax
- It's used on the left-hand side of an expression
- Since slicing returns a list, slice assignment requires a list (or other iterable)
- The right-hand side should be the value to assign to the slice on the left-hand side of the expression
'''

nums = [1, 2, 3, 4, 5]

nums[:1] = [6]        # [6, 2, 3, 4, 5]   (replace elements 0 through 1)
nums[1:3] = [7, 8]    # [6, 7, 8, 4, 5]   (replace elements 1 through 3)
nums[-2:] = [9, 0]    # [6, 7, 8, 9, 0]   (replace the last 2 elements)

'''
2) Changing length
- Use slice assignment to replace part of the list with a different list
  whose length is also different from the returned slice
- Insert elements into a list without replacing anything in it
'''

nums = [1, 2, 3, 4, 5]

nums[1:4] = [6, 7]    # [1, 6, 7, 5]        (replace 3 elements with 2)
nums[-1:] = [8, 9, 0] # [1, 6, 7, 8, 9, 0]  (replace 1 element with 3)
nums[:1] = []         # [6, 7, 8, 9, 0]     (replace 1 element with 0)

nums = [1, 2, 3, 4, 5]

nums[2:2] = [6, 7]    # [1, 2, 6, 7, 3, 4, 5]   (insert 2 elements)
nums[7:] = [8, 9]     # [1, 2, 6, 7, 3, 4, 5, 8, 9] (append 2 elements)
nums[:0] = [0]        # [0, 1, 2, 6, 7, 3, 4, 5, 8, 9] (prepend 1 element)
nums[:] = [ 4, 2]     # [4, 2]         (replace whole list with a new one)

'''
3) Using steps
- You can use it to replace elements that match the iteration after each stride
- ★ If step is not 1, the inserted list must have the exact same length as that of the returned list slice
'''

nums = [1, 2, 3, 4, 5]

nums[2:5:2] = [6, 7]     # [1, 2, 6, 4, 7] (replace every 2nd element, 2 through 5)
nums[2:5:2] = [6, 7, 8]  # Throws a ValueError (can't replace 2 elements with 3)
nums[1::-1] = [9, 0]     # [0, 9, 6, 4, 7] (reverse replace, 1 through start)
