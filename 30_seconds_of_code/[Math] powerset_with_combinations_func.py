
'''
powerset
Returns the powerset of a given iterable

- Use list() to convert the given value to a list
- Use range() and itertools.combinations() to create a generator
  that returns all subsets
- Use itertools.chain.from_iterable() and list()
  to consume the generator and return a list

combinations
- 리스트에 있는 값들의 모든 조합 구하기
- ※ permutations : 같은 조합이라도 순서가 다르면 둘 다 return

chain.from_iterable
- https://docs.python.org/ko/3.8/library/itertools.html
- chain.from_iterable(['ABC', 'DEF']) --> A B C D E F

https://www.30secondsofcode.org/python/s/powerset
'''

from itertools import chain, combinations

def powerset(lst):
    s = list(lst)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


# Example
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]


# reference =====================================================

list(combinations(['1','2','3'], 2))
# [('1', '2'), ('1', '3'), ('2', '3')]

list(chain.from_iterable(combinations(['1','2','3'], 2)))
# ['1', '2', '1', '3', '2', '3']


