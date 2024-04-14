from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        memo = defaultdict(int)
        for num in nums:
            memo[num]=memo[num-1]+1
            if memo[num]>count:
                count=memo[num]
        return count
        
        #mp = defaultdict(list)
        