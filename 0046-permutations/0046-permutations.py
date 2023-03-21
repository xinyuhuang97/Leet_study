class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [[nums[0]]]
        else:
            sol=[]
            for i in range(len(nums)):
                print(i,len(nums))
                sous_list=self.permute(nums[:i]+nums[i+1:])
                for sl in sous_list:
                    sol.append([nums[i]]+sl)
            return sol

    

    