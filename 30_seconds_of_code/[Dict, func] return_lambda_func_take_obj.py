
'''
check_prop
Creates a function that will invoke a predicate function
for the specified property on a given object

- Return a lambda function that takes an object
  and applies the predicate function, fn to the specified property

Predicate functions 
- Predicate functions are functions that return a single TRUE or FALSE
- You use predicate functions to check if your input meets some condition
   
https://www.30secondsofcode.org/python/s/check-prop
'''

def check_prop(fn, prop):
    return lambda obj: fn(obj[prop])


# Example
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
