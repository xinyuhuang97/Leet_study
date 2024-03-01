class Solution:
    def jump(self, nums: List[int]) -> int:
        
        nb=len(nums)
        dp=[0 for i in range(nb)]
        arrive=[0 for i in range(nb)]
        dp[nb-1]=0
        arrive[nb-1]=1
        for i in range(nb-1, -1, -1):
            for dis in range(nums[i], 0, -1):
                if i+dis<nb:
                    if arrive[i+dis]==1:
                        if dp[i]==0:
                            dp[i]=dp[i+dis]+1
                        else:
                            if dp[i+dis]+1<dp[i]:
                                dp[i]=dp[i+dis]+1
                        arrive[i]=1
        print(dp)
        print(arrive)
        return dp[0]
                    