class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]   i 
        # lr [1,1,2,8] i 
        # prev = og[i-1]; lr[i] = if i-1 < 0 then 1 else prev*lr[i-1]
        # rl [48,24,6,1] k
        #   Similar but using i+1 and checking if i >= len(nums)
        #.   48,24,12,8
        lr = [1]*len(nums)
        rl = [1]*len(nums)
        
        #lr
        i = 1
        while i < len(nums):
            lr[i] = nums[i-1] * lr[i-1]
            i = i + 1
        
        i = len(nums) - 2
        while i >= 0:
            rl[i] = nums[i + 1] * rl[i + 1]
            i = i - 1
        
        i = 0
        while i < len(nums):
            lr[i] = lr[i] * rl[i]
            i = i + 1
        
        return lr