import collections
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_val=min(coins)
        if amount==0:
            return 0
        if amount<min_val:
            return -1
        dp=[-1]*(amount+1)
        dp[0]=0
        for coin in coins:
            if coin<=amount:
                dp[coin]=1
        
        deque=collections.deque(coins)
        while deque:
            val=deque.popleft()
            #print(dp,coins,val)
            for coin in coins:
                if val+coin>amount:
                    continue
                if dp[val+coin]>dp[val]+1 or dp[val+coin]==-1:
                    dp[val+coin]=dp[val]+1
                    deque.append(val+coin)
            #print(deque)
        return dp[amount]