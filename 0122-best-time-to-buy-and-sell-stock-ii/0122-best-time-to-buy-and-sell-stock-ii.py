class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]

        # Base case: no stocks held on day 0
        dp[0][0] = 0
        # Buying a stock on day 0, so the profit is negative of the stock price
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # Calculate the maximum profit on day i with no stocks held
            dp[i][0] = max(dp[i - 1][0], prices[i] + dp[i - 1][1])
            # Calculate the maximum profit on day i with stocks held
            dp[i][1] = max(dp[i - 1][1], dp[i][0] - prices[i])

        # The maximum profit is either selling the stock on the last day or not holding any stocks
        return max(dp[-1][0], 0)

