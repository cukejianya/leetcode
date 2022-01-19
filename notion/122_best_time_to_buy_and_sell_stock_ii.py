class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(float("-inf"))
        buy = 0
        sell = 0
        profits = 0
        while(sell < len(prices) - 1):
            if prices[sell] > prices[sell + 1]:
                profits += prices[sell] - prices[buy]
                buy = sell + 1
            sell += 1
        return profits