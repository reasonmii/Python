
'''
unfold
Builds a list, using an iterator function and an initial seed value

- The iterator function accepts one argument (seed)
  and must always return a list with two elements ([value, nextSeed]) or False to terminate
- Use a generator function, fn_generator,
  that uses a while loop to call the iterator function
  and yield the value until it returns False
- Use a list comprehension to return the list
  that is produced by the generator, using the iterator function

https://wikidocs.net/16069
- generator : iterator를 생성해주는 함수, 함수안에 yield 키워드를 사용함
- yield 가 호출되면 암시적으로 return이 호출

https://www.30secondsofcode.org/python/s/unfold
'''

def unfold(fn, seed):
    def fn_generator(val):
        while True:
            val = fn(val[1])
            if val == False: break
            yield val[0]
    return [i for i in fn_generator([None, seed])]
        

# Example
f = lambda n: False if n > 50 else [-n, n + 10]
unfold(f, 10) # [-10, -20, -30, -40, -50]
