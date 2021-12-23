
'''
median
Finds the median of a list of numbers

- Sort the numbers of the list using list.sort()
- Find the median, which is either the middle element of the list if the list length is odd
  or the average of the two middle elements if the list length is even
- statistics.median() provides similar functionality to this snippet

https://www.30secondsofcode.org/python/s/median
'''

def median(lst):
    lst.sort()
    lst_len = len(lst)
    if lst_len % 2 == 0:
        return (lst[int(lst_len/2) - 1] + lst[int(lst_len/2)]) / 2
    return float(lst[int(lst_len/2)])


# Example
median([1, 2, 3])    # 2.0
median([1, 2, 3, 4]) # 2.5
