class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
        biggest_occurence=0
        number=0
        
        """for keys in count:
            if count[keys]>biggest_occurence:
                biggest_occurence=count[keys]
                number=keys
                """
        number=max(count,key=count.get)
        return number