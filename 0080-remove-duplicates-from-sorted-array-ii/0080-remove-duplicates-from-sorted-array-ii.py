class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        hashtable={}
        for i in range(len(nums)):
            if (nums[i] not in hashtable ):
                if index!=i:
                    nums[index]=nums[i]
                    hashtable[nums[i]]=1
                else:
                    hashtable[nums[i]]=1
                index+=1
            else:
                if hashtable[nums[i]]==1:
                    if index!=i:
                        nums[index]=nums[i]
                        hashtable[nums[i]]=2
                    else:
                        hashtable[nums[i]]=2
                    index+=1
        return index