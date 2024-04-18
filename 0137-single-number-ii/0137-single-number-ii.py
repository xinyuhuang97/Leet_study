class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(32):
            cpt=0
            for num in nums:
                cpt+= num>>i&1
            cpt%=3
            ans|=cpt<<i
        if ans>=2**31:
            ans-=2**32
        return ans
            