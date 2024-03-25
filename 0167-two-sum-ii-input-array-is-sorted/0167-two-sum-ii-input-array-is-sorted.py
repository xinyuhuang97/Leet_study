class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0
        right=n-1
        while left<right:
            cur_sum=numbers[left]+numbers[right]
            if cur_sum==target:
                return [left+1,right+1]
            elif cur_sum>target:
                right-=1
            else:
                left+=1
        return []
            
        