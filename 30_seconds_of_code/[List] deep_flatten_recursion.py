
'''
deep_flatten
Deep flattens a list

- Use recursion
- Use isinstance() with collections.abc.Iterable to check if an element is iterable
- If it is iterable, apply deep_flatten() recursively, otherwise return [lst]

collections.abc.Iterable
- isinstance(obj, Iterable)를 검사하면
  Iterable로 등록되었거나 __iter__() 메서드가 있는 클래스를 감지
- __getitem__() 메서드로 이터레이트 하는 클래스는 감지 못함
- ※ 객체가 이터러블인지를 확인하는 유일하게 신뢰성 있는 방법은 iter(obj)

https://www.30secondsofcode.org/python/s/deep-flatten
'''

from collections.abc import Iterable

def deep_flatten(lst):    
    return ([a for i in lst for a in deep_flatten(i)] if isinstance(lst, Iterable) else [lst])

            
# Example
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
