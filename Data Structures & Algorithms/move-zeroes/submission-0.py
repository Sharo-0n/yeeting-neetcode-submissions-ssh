class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [0,0,1,2,0,5]
        #.        1 ^ 0 2 0 5
        #.        1 0 0 2 0 5
        #.        1 2 0 0 0 5
        #.            ^
        #         1 2 0 0 0 5
        #.            ^  
        ptr = 0
        for idx, num in enumerate(nums):
            # when on zero do not move ptr
            # move ptr otherwise
            if num > 0: 
                if ptr != idx:
                    nums[ptr] = num
                    nums[idx] = 0
                ptr += 1