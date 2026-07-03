class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            
            maxProfit = max(maxProfit, prices[sell] - prices[buy])
            sell += 1
        
        return maxProfit




        