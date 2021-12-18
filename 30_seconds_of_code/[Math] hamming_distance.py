'''
hamming_distance
Calculates the Hamming distance between two values

- Use the XOR operator (^) to find the bit difference between the two numbers
- Use bin() to convert the result to a binary string
- Convert the string to a list and use count() of str class
  to count and return the number of 1s in it
  
Hamming distance
- The Hamming distance between two integers is the number of positions
  at which the corresponding bits are different
- ex) Input: x = 1, y = 4
      1   (0 0 0 1)
      4   (0 1 0 0)
      output : 2

https://www.30secondsofcode.org/python/s/hamming-distance
'''

def hamming_distance(a, b):  
    return bin(a ^ b).count('1')


# Example
hamming_distance(2, 3) # 1
