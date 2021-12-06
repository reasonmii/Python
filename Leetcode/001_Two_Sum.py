

''' 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Company
Amazon, Google, Apple, Adobe, Microsoft, Bloomberg, Facebook,
Oracle, Expedia, Uber, Intuit, Twitter, Yahoo, Goldman Sachs, SAP,
Airbnb, Nagarro, Citrix, Qualcomm, ByteDance

Easy
'''

class Solution(object):
    def twoSum(self, nums, target):
        
        dic = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return [dic[diff], i]
            dic[n] = i                 # ex. dic : {7: 2, 2: 1, 11: 3}
        return



# Example 1    
nums = [2,7,11,15]
target = 9
Solution().twoSum(nums = nums, target = target)   # [0, 1]

# Example 2
nums = [3,2,4]
target = 6
Solution().twoSum(nums = nums, target = target)   # [1, 2]

# Example 3
nums = [3,3]
target = 6
Solution().twoSum(nums = nums, target = target)   # [0, 1]

