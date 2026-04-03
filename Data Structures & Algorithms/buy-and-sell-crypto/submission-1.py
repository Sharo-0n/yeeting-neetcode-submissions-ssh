class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,8,7,5,2]
        # [10,1,5,6,7,1]
        #   ^         ^
        # early_min later_max

        max_diff = 0
        for idx, early in enumerate(prices):
            for later in prices[idx:]:
                max_diff = max(max_diff, later - early)
        return max_diff
