from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_threshold = len(nums) / 2
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1
            if hm[num] > maj_threshold:
                return num
        
        return -1