class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0
        
        dp = {}


        def decide(i, buy):
            if i >= len(prices):
                return 0 
            
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            if buy:
                buy_profit = decide(i+1, not buy) - prices[i]
                cooldown_profit = decide(i+1, buy)
                dp[(i, buy)] = max(buy_profit, cooldown_profit)
            else:
                sell_profit = decide(i+2, not buy) + prices[i]
                cooldown_profit = decide(i+1, buy)
                dp[(i, buy)] = max(sell_profit, cooldown_profit)
            
            return dp[(i, buy)]

        return decide(0, True)