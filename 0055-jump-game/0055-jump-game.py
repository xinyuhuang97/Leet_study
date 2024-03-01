class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nb=len(nums)
        dp=[0 for i in range(nb)]
        dp[nb-1]=1
        closest=nb-1
        for i in range(nb-2,-1,-1):
            if nums[i]==0:
                continue
            if nums[i]+i<closest:
                dp[i]=0
            else:
                dp[i]=1
                closest=i
        return dp[0]
                    
        