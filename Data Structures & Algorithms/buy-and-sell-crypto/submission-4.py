class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        # min_so_far = 1
        # max_profit = 
        # 1 ptr moving left to right checking if curr is < msf or curr - msf

        min_so_far = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_so_far:
                min_so_far = price
            else:
                max_profit = max(max_profit, price - min_so_far)
        
        return max_profit