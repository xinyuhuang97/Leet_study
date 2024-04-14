from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mp = defaultdict(list)
        bl = defaultdict(list)
        mx = 0
        for num in nums:
            if bl[num]:
                continue
            bl[num] = True
            l, r = num, num
            if bl[num+1]:
                r=mp[num+1][1]
            if bl[num-1]:
                l=mp[num-1][0]
            mp[r]= [l, r]
            mp[l]= [l, r]
            mx = max(r-l+1, mx)
        return mx