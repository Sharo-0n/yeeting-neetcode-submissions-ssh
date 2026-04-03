import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 :
            return None
        heapq.heapify(nums)
        nlargest = heapq.nlargest(k, nums)
        return nlargest[len(nlargest) - 1]