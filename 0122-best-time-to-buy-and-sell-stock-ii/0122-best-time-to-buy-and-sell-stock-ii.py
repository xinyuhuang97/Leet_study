from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nb = len(prices)
        if nb <= 1:
            return 0

        max_profit = 0

        for i in range(1, nb):
            # If the price today is higher than yesterday, we can make a profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit



