# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

# Method 1 : 91ms
class Solution(object):
    def uniqueOccurrences(self, arr):
        
        chk = dict()
        
        for n in arr:
            if n not in chk.keys():
                chk[n] = 1
            else:
                chk[n] += 1
        
        rst = True
        for k1, v1 in chk.items():
            for k2, v2 in chk.items():
                if k1 != k2 and v1 == v2:
                    rst = False
                    break

        return rst

# Method2 : 53ms 
from collections import Counter
        
class Solution(object):
    def uniqueOccurrences(self, arr):
    
        out = Counter(arr).values() # dict_values([3, 2, 1])
        out = Counter(list(out))    # Counter({3: 1, 2: 1, 1: 1})
        out = len(out)              # 3

        return out == len(Counter(arr))
            

