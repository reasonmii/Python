# 따로 결과 저장하는 게 아니라 input으로 받은 nums 자체를 바꿔야 함

class Solution(object):
    def removeDuplicates(self, nums):
        
        k = 0
        
        for i, n in enumerate(nums):
            if n != nums[k]:
                k += 1
                nums[k] = n
        
        return k + 1
