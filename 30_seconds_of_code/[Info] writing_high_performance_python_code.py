
'''
This implementation may work well enough, but doesn't account for duplicates in b.
This makes the code take more time than necessary in cases with many duplicates in the second list.
'''

def difference(a, b):
  return [item for item in a if item not in b]

'''
To solve this issue, we can make use of the set() method, which will only keep the unique values in the list.
This version, while it seems like an improvement, may actually be "slower" than the previous one.
If you look closely, you will see that "set() is called for every item".
'''

def difference(a, b):
  return [item for item in a if item not in set(b)]

'''
Here's an example where we wrap set() with another method to better showcase the problem.
'''

def difference(a, b):
  return [item for item in a if item not in make_set(b)]

def make_set(itr):
  return set(itr)

'''
The solution to this issue is to call set() once before the list comprehension
and store the result to speed up the process.
'''

def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]

'''
Another option worth mentioning in terms of performance is the use of a "list comprehension" versus "filter() and list()".
Implementing the same code using the latter option would result in something like this.
'''

def difference(a, b):
  _b = set(b)
  return list(filter(lambda item: item not in _b, a))

'''
Using "timeit" to analyze the performance of the last two code examples,
it's pretty clear that using "list comprehension" can be up to "ten times faster" than the alternative.
This is due to it works very similar to a simple for loop without the overhead of the extra function calls.
This explains why we prefer it, apart from readability.

This pretty much applies to most mathematical list operation snippets, such as difference, symmetric_difference and intersection.
'''

