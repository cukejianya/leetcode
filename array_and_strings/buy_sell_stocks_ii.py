class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        for idx in range(len(prices) - 1):
            if prices[idx] < prices[idx + 1]: 
                max_profit += (prices[idx + 1] - prices[idx])
        return max_profit