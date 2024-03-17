class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        range_list=[]
        if nums==[]:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        first_number=nums[0]
        last_number=nums[0]
        for i,num in enumerate(nums):
            if i==0:
                continue  
            if last_number+1==num:
                last_number+=1
            else:
                if  first_number==last_number:
                    range_list.append(str(first_number))
                else:
                    range_list.append(str(first_number)+"->"+str(last_number))
                first_number=num
                last_number=num
        if  first_number==last_number:
            range_list.append(str(first_number))
        else:
            range_list.append(str(first_number)+"->"+str(last_number))
        return range_list
            