class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hm: diff(target-prev_val): index of prev_val
        diff = {}

        # loop 
        for idx, n in enumerate(nums):
            if n in diff:
                return [diff[n], idx]
            else:
                diff[target - n] = idx
        return [-1, -1]