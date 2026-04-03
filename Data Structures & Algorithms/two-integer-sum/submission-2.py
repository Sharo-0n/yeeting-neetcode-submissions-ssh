class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - nums[i] : i
        hm = {}

        for idx, num in enumerate(nums):
            # check to see if key of num exists
            if num in hm:
                # return value and current index
                return [hm[num], idx]
            # add new elem to hm
            else:
                hm[target-num] = idx
        
        return None