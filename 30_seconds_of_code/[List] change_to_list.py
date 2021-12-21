'''
cast_list
Casts the provided value as a list if it's not one

- Use isinstance() to check if the given value is enumerable
- Return it by using list() or encapsulated in a list accordingly

※ list()
- 리스트로 변환 가능한 다른 자료형을 리스트로 바꿔주는 기능

https://www.30secondsofcode.org/python/s/cast-list
'''

def cast_list(obj):
  return list(obj) if isinstance(obj, (tuple, list, set, dict)) else [obj]

# Example
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
