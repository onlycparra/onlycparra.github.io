class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_time = 0
        sell_time = 1
        max_profit = 0

        while sell_time < len(prices):
            prof_loss = prices[sell_time] - prices[buy_time]
            if 0 < prof_loss:
                max_profit = max(max_profit, prof_loss)
            else:
                buy_time = sell_time
            sell_time += 1
        
        return max_profit
