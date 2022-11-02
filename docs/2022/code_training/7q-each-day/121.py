class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = float('inf')
        best_profit = 0

        for day_price in prices:
            if day_price < best_buy:
                best_buy = day_price
            elif (day_price - best_buy) > best_profit:
                best_profit = day_price - best_buy
        return best_profit
