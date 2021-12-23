
'''
sort_by_indexes
Sorts one list based on another list containing the desired indexes

- Use zip() and sorted() to combine and sort the two lists, based on the values of indexes
- Use a list comprehension to get the first element of each pair from the result
- Use the reverse parameter in sorted() to sort the dictionary in reverse order, based on the third argument

https://www.30secondsofcode.org/python/s/sort-by-indexes
'''

def sort_by_indexes(lst, indexes, reverse=False):
    # 이 때 lambda x는 앞에 zip(indexes, lst)를 가리키게 됨
    return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: x[0], reverse=reverse)]
    

# Example
a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]

sort_by_indexes(a, b)
# ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']

sort_by_indexes(a, b, True)
# ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']


# reference =====================================================

for pair in sorted(zip(b, a)):
    print(pair)

# (1, 'apples')
# (2, 'bread')
# (3, 'eggs')
# (4, 'jam')
# (5, 'milk')
# (6, 'oranges')

for (_, val) in sorted(zip(b, a)):
    print(val)
# apples
# bread
# eggs
# jam
# milk
# oranges

