class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lg=len(nums)
        for i in range(lg-1):
            for j in range(i+1, lg):
                if nums[i]+nums[j]==target:
                    return [i,j]