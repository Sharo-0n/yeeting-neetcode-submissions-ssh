class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 1, 5, 6, 7, 1]
        #  lr
        #  l  r
        #.    lr
        l, r = 0, 1
        max_delta = 0
        while r < len(prices):
            max_delta = max(max_delta, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r = r + 1
                
        return max_delta
