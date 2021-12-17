
'''
longest_item
Takes any number of iterable objects or objects with a length property
and returns the longest one

- Use max() with len() as the key to return the item with the greatest length
- If multiple items have the same length, the first one will be returned

https://www.30secondsofcode.org/python/s/longest-item
'''

def longest_item(*args):
    return max(args, key=len)
  

# Example
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
