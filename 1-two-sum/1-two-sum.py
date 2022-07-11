class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        #Regular methode
        lg=len(nums)
        for i in range(lg-1):
            for j in range(i+1, lg):
                if nums[i]+nums[j]==target:
                    return [i,j]
        """
        #Hash map methode
        seen={}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            seen[value]=i
        