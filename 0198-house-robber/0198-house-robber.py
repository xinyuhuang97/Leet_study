class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        pd=[0]*n
        pd[0]=nums[0]
        pd[1]=max(nums[0],nums[1])
        for i in range(2,n):
            pd[i]=max(pd[i-1],pd[i-2]+nums[i])
        return pd[n-1]