class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        dp=[1]*n
        #lgest=1
        for i in range(1,n):          
            for j in range(i):
                #print(nums[i],nums[j])
                #print(dp,dp[j]+1)
                if nums[j]<nums[i] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    #print(nb)
            #lgest=max(lgest,dp[i])
        #return lgest
        return max(dp)
        
