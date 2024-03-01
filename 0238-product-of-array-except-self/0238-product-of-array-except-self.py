class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nb=len(nums)
        prefix=[1]*nb
        suffix=[1]*nb
        
        for i in range(1,nb-1):
            prefix[i]=prefix[i-1]*nums[i-1]
            suffix[nb-1-i]=suffix[nb-i]*nums[nb-i]
        prefix[nb-1]=prefix[nb-2]*nums[nb-2]
        suffix[0]=suffix[1]*nums[1]
        print(prefix, suffix)
        for i in range(nb):
            prefix[i]=prefix[i]*suffix[i]
        return prefix
            