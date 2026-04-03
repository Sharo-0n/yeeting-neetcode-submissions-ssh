class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6]
        max_val = 0

        l, r = 0, len(heights) - 1
        
        while l < r:
            max_val = max(max_val, min(heights[l], heights[r])*(r-l))
            if heights[l] < heights[r]:
                l = l + 1
            elif heights[l] >= heights[r]:
                r = r - 1

        return max_val