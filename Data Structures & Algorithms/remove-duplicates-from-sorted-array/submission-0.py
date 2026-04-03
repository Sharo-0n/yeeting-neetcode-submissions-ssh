class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = None
        
        idx = 0
        while idx < len(nums):
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                del nums[idx + 1]
            idx += 1

        return len(nums)