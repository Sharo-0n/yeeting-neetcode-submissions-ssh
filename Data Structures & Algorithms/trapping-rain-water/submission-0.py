class Solution:
    def trap(self, height: List[int]) -> int:
        # min(l,r) - h[i]
        # [0,2,0,3,1,0,1,3,2,1]
        #  ^    l = 0, r = shrug
        l = [0] * len(height)
        r = [0] * len(height)
        max_l = 0
        max_r = 0
        area = 0
        # left to right, track max
        for idx, h in enumerate(height):
            l[idx] = max_l
            max_l = max(max_l, h)
        
        for idx in range(len(height) - 1, -1, -1):
            r[idx] = max_r
            val = min(r[idx], l[idx]) - height[idx]
            if val > 0:
                area += min(r[idx], l[idx]) - height[idx]
            max_r = max(max_r, height[idx])

        return area