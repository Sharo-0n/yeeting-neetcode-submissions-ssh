import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 :
            return None
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return heapq.heappop(nums)