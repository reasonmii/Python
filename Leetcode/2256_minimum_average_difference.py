
# https://leetcode.com/problems/minimum-average-difference/
# list를 slicing 하는 방법은 time exceed
# int로 계산하는 게 맞음

class Solution(object):
    def minimumAverageDifference(self, nums):
               
        tot = sum(nums)
        left = 0
        min_i, min_n = 0, float("inf")
        
        for i, n in enumerate(nums):
            left += n
            right = tot - left
            
            if i != len(nums) - 1:
                if abs(left // (i+1) - right // (len(nums) - (i+1))) < min_n:
                    min_n = abs(left // (i+1) - right // (len(nums) - (i+1)))
                    min_i = i
            else:
                if left // (i+1) < min_n:
                    min_i = i
                    
        return min_i
