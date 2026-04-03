class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} # target - nums[index] : index
        for i, num in enumerate(nums):
            # check if num is key in hm
            if num in hm:
                return [hm[num], i]
            else:
                hm[target-num] = i