# input으로 받은 nums 자체를 바꿔야 

class Solution(object):
    def removeDuplicates(self, nums):
        
        k = 0
        
        for i, n in enumerate(nums):
            if n != nums[k]:
                k += 1
                nums[k] = n
        
        return k + 1
