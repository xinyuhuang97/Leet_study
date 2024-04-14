class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_memo = {}
        for i, n in enumerate(nums):
            if n in dict_memo and i-dict_memo[n]<=k:
                return True
            dict_memo[n] = i
        return False