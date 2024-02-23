class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
        number=max(count,key=count.get)
        return number