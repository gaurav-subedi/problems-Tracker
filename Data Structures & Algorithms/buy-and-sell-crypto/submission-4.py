class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l , r = 0,1 
        while r < len(prices):
            b , s = prices[l], prices[r]
            profit = max(profit, s - b)
            if(s - b) < 0:
                l += 1
            else:
                r += 1
        return profit

