
'''
take
Returns a list with n elements removed from the beginning

- Use slice notation to create a slice of the list
  with n elements taken from the beginning

https://www.30secondsofcode.org/python/s/take
'''

def take(lst, n=1):
    return lst[:n]


# Example
take([1, 2, 3], 5) # [1, 2, 3]
take([1, 2, 3], 0) # []


'''
take_right
Returns a list with n elements removed from the end

- Use slice notation to create a slice of the list
  with n elements taken from the end

https://www.30secondsofcode.org/python/s/take-right
'''

def take_right(lst, n=1):
    return lst[-n:]


# Example
take_right([1, 2, 3], 2) # [2, 3]
take_right([1, 2, 3]) # [3]


'''
initial
Returns all the elements of a list except the last one

- Use lst[:-1] to return all but the last element of the list

https://www.30secondsofcode.org/python/s/initial
'''

def initial(lst):
    return lst[:-1]


# Example
initial([1, 2, 3]) # [1, 2]

